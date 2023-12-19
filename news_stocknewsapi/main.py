import config
import requests
import csv

# 
for page in range(2000,2008):
    url = f"https://stocknewsapi.com/api/v1?tickers=AAPL,MSFT,GOOG,AMZN,TSLA,META,NVDA,PEP,COST,IVVD,SOFI,RIVN,AAL,CAN,INTC&items=3&page={page}&token={config.api}&datatype=csv"

    response = requests.request("GET", url)
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