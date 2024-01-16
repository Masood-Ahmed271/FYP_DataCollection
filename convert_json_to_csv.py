import os
import csv
import json

parent_folder = 'yahoo_finance_stock_prices/data'
folder_list = os.listdir(parent_folder)
print(folder_list)

for each_file in folder_list:
    # Read the CSV file
    data = []
    csv_file_path = parent_folder + "/" + each_file
    json_file_path = 'yahoo_finance_stock_prices/data_json/' + each_file[:-3] + "json"
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    # Write the data to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)