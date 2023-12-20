import pandas as pd
import glob

# Specify the path to the folder containing the CSV files
folder_path = './data'

# Use glob to get a list of all CSV files in the folder
file_list = glob.glob(folder_path + '/*.csv')

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame(columns=["news_url", "image_url", "title", "text", "source_name", "date", "topics", "sentiment", "type", "tickers"])

# Iterate over each CSV file and merge its data into the merged_data DataFrame
for file in file_list:
    df = pd.read_csv(file, skiprows=1)  # Skip the header row
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# Specify the path and filename for the merged CSV file
output_file = './data/merged/news_merged.csv'

# Save the merged data to a CSV file
merged_data.to_csv(output_file, index=False)

print("Merged CSV file saved successfully.")