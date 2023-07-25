import yfinance as yf
import pandas as pd
from pydantic import ValidationError
import json
import os
from config import Config

class HistDataDownloader:

    @staticmethod
    def download_data(config: Config):
        # Create a directory to store the downloaded data
        if not os.path.exists('./data/hist_data'):
            os.makedirs('./data/hist_data')
            
        # Download the historical data for each ticker and save it to a csv file
        for ticker in config.tickers:
            data = yf.download(ticker, start=config.start_date, end=config.end_date)
            data.to_csv(f'./data/hist_data/{ticker}.csv')