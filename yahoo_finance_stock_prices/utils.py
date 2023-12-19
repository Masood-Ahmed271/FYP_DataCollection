import yfinance as yf
import pandas as pd

class StockDataDownloader:
    def __init__(self, tickers):
        self.tickers = tickers

    def download_data(self):
        for ticker in self.tickers:
            data = yf.download(tickers=ticker, period="max", interval="1d")
            file_path = f"./data/{ticker}_stock_price.csv"
            data.to_csv(file_path)


class preprocessing:
    def __init__(self, tickers):
        self.tickers = tickers
    
    def check_null_values(self):
        for ticker in self.tickers:
            path = f"./data/{ticker}_stock_price.csv"
            df = pd.read_csv(path)
            null_count = df.isnull().sum().sum()
            print(f'Number of null values in {ticker}:', null_count)