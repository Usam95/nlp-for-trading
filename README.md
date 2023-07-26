# Project: Analyzing Financial Returns using Natural Language Processing
This project focuses on testing two main hypotheses concerning financial returns of firms and their sentiment scores derived from Item 7 of their 10-K reports.

10-K reports are annual reports that publicly traded companies are required to file with the U.S. Securities and Exchange Commission (SEC). They provide a comprehensive summary of a company's financial performance and include mandatory items such as financial statements, management discussion and analysis, disclosures about market risk, and other relevant information. Item 7 of these reports contains the "Management's Discussion and Analysis of Financial Condition and Results of Operations" where companies provide detailed narratives of their financial and operational status.

The main hypotheses under consideration in this project are:

H0: Returns of firms with stronger net positive tone are statistically equal to the returns of firms with weaker net positive tone.

H1: Returns of firms with stronger net positive tone are statistically greater than the returns of firms with weaker net positive tone.

A financial return, in simple terms, is the money made or lost on an investment over some period of time. It is calculated as the change in dollar value of an investment, including any cash flows such as dividends, divided by the initial investment amount, and is often expressed as a percentage.

In the context of this project, we extract and preprocess the data from Item 7 of 10-K reports and estimate the sentiment (or tone) given in these reports. By doing so, we aim to investigate if there is any correlation between the sentiment of these reports and the returns of the respective firms.

The project involves grouping the companies based on the net tone (positive or negative) in their 10-K reports and comparing the returns of these groups.


The t-test will help determine if the difference between the returns of the two groups is statistically significant or not. A significant result will reject the null hypothesis (H0), suggesting that companies with a stronger net positive tone in their 10-K reports have statistically greater returns. A non-significant result will fail to reject the null hypothesis, suggesting no statistical difference in the returns based on the tone of the 10-K reports.

This project thus utilizes the power of Natural Language Processing (NLP) to uncover potential links between the sentiment in financial reports and the financial performance of companies.
