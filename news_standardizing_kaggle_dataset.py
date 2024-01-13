import pandas as pd
import json

data = []
with open('kaggle_dataset/News_Category_Dataset_v3.json') as f:
    for line in f:
        try:
            json_data = json.loads(line)
            data.append(json_data)
        except json.JSONDecodeError:
            pass

df = pd.json_normalize(data)
df.to_csv('kaggle_dataset/News_Category_Dataset_v3.csv', index=False)