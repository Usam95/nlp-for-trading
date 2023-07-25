import os
from sec_edgar_downloader import Downloader
import re
import shutil
import glob 
from datetime import datetime
from time import sleep


from config_loader import load_config

class SecReportRetriever: 
    """
    This class is used to retrieve and analyse the 10-K reports stocks that were 
    filtered out by Scanner to day trade. The SEC requires each company from US exchanges
    to annualy publish 10-K reports using a defined form.
    """
    def __init__(self, config_path: str, root_dir = "./tmp"):
    
        self.config = load_config(config_path)
        if self.config is None:
            raise ValueError('Invalid configuration file.')
        self.scanned_tickers = self.config.tickers
        # Rest of your code
        self.tickerReportsDic = {}
        self.root_dir = root_dir            
        self.dl = Downloader(self.root_dir)
        self.tickerNewestReportDateDic = {}

    
    def set_ticker_list(self, ticker_list):
        self.scanned_tickers = ticker_list
        
        
    def getReports(self, report_type="10-K", amount=1): 
        for ticker in self.scanned_tickers: 
            self.dl.get(report_type, ticker, amount=amount)
            sleep(0.3)
        print("The defined reports for scanned tickers are downloaded.")
        
    
    def createEmptyRootDir(self): 
        print("createEmptyRootDir: called")
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)
        else: 
            files = glob.glob(self.root_dir + "/*")
            for f in files:
                if os.path.isdir(f):
                    shutil.rmtree(f)
                else:
                    os.remove(f)
                
                
    def initTickerReportsDic(self): 
        root_path = os.path.join(self.root_dir, "sec-edgar-filings")
        try:
            files = os.listdir(root_path)
            for file in files: 
                if os.path.isdir(os.path.join(root_path, file)) and ".DS_Store" not in file:
                    for ticker in self.scanned_tickers: 
                        if ticker == file: 
                            self.tickerReportsDic[ticker] = {}
            for ticker, _ in self.tickerReportsDic.items():
                reportTypesDirs = os.listdir(os.path.join(root_path, ticker))
                reportTypesDirs = [d for d in reportTypesDirs if ".DS_Store" not in d]
                for reportTypeDir in reportTypesDirs:
                    reportFiles = []      
                    path = os.path.join(root_path, ticker, reportTypeDir)
                    for current_dir_path, _, current_files in os.walk(path):
                        for file in current_files:
                            if file.endswith((".txt", ".xml", ".html")):
                                file_path = os.path.join(current_dir_path,file )
                                reportFiles.append(file_path)
                    self.tickerReportsDic[ticker][reportTypeDir] = reportFiles
        except FileNotFoundError: 
            print("The edgar folder with downloaded reports is not available. ")
    
    def getNewestReportPublishDates(self): 
        root_path = os.path.join(self.root_dir, "sec-edgar-filings")
        for ticker, reportTypes_dic in self.tickerReportsDic.items(): 
            ticker_report_max_datetimes = []
            for _, reports in reportTypes_dic.items(): 
                for report in reports: 
                    if "full-submission.txt" in report: 
                        with open(report, "r") as f: 
                            file_content = f.read()
                            datetime_list = re.findall(r"[A-Z\s]+:(?:\s*)(\d{8})\D", file_content)
                            datetime_list = list(set(datetime_list)) # Remove duplicates using set
                            datetime_list = [dt for dt in datetime_list if 2010 < int(dt[:4]) < 2023]
                            if datetime_list:
                                datetime_list = [datetime.strptime(dt, '%Y%m%d') for dt in datetime_list]
                                ticker_report_max_datetimes.append(max(datetime_list))
            if ticker_report_max_datetimes:         
                self.tickerNewestReportDateDic[ticker] = max(ticker_report_max_datetimes)
        return self.tickerNewestReportDateDic