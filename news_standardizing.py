import os
import json
import pandas as pd

parent_folder = 'webz_io'
folder_list = os.listdir(parent_folder)

df = pd.DataFrame()

for folder in folder_list:
    folder_path = os.path.join(parent_folder, folder)
    file_list = os.listdir(folder_path)

    for file in file_list:
        file_path = os.path.join(folder_path, file)

        with open(file_path, 'r') as f:
            contents = f.read()
        data = json.loads(contents)
        # Convert the JSON data to a DataFrame
        new_df = pd.json_normalize(data)

        # Append new DataFrame to the existing DataFrame
        df = pd.concat([df, new_df], ignore_index=True)
df.to_csv('webzio_converted_json_to_csv.csv')
# Total files were 47851