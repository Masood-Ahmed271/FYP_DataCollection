import utils

# Downlaoding data from yfinance
possible_tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA', 'META', 'NVDA', 'PEP', 'COST', 'IVVD', 'SOFI', 'RIVN', 'AAL', 'CAN', 'INTC']
downloader = utils.StockDataDownloader(possible_tickers)
downloader.download_data()


# Checking Null Values
data = utils.preprocessing(possible_tickers)
data.check_null_values()