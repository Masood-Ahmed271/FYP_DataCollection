import config
import requests
import csv

class StockNewsAPIExporter:
    def __init__(self):
        self.base_url = "https://stocknewsapi.com/api/v1"
        self.tickers = "AAPL,MSFT,GOOG,AMZN,TSLA,META,NVDA,PEP,COST,IVVD,SOFI,RIVN,AAL,CAN,INTC"
        self.items_per_page = 3
        self.token = config.api
        self.datatype = "csv"

    def export_news_data(self, start_page, end_page):
        for page in range(start_page, end_page + 1):
            url = f"{self.base_url}?tickers={self.tickers}&items={self.items_per_page}&page={page}&token={self.token}&datatype={self.datatype}"

            response = requests.get(url)
            response = response.text
            # Split the response into individual lines
            lines = response.strip().split('\n')
            # Extract the header and rows
            header = lines[0].split(',')
            rows = [line.split(',') for line in lines[1:]]

            # Specify the output CSV file path
            output_file = f'./data/news_{page}.csv'

            # Write the data to the CSV file
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)  # Write the header
                writer.writerows(rows)  # Write the rows

            print(f"CSV file '{output_file}' has been created successfully.")