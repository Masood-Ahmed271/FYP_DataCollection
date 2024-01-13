import os
import json
import pandas as pd

parent_folder = 'webz_io'
folder_list = os.listdir(parent_folder)

number = 0
for folder in folder_list:
    folder_path = os.path.join(parent_folder, folder)
    file_list = os.listdir(folder_path)
    for file in file_list:
        df = pd.DataFrame()
        file_path = os.path.join(folder_path, file)

        with open(file_path, 'r') as f:
            contents = f.read()
        data = json.loads(contents)
        # Convert the JSON data to a DataFrame
        new_df = pd.json_normalize(data)

        # Append new DataFrame to the existing DataFrame
        df = pd.concat([df, new_df], ignore_index=True)

        df.drop(['ord_in_thread', 'highlightText', 'highlightTitle', 'entities.persons', 
                'entities.locations', 'entities.organizations','thread.social.gplus.shares',
                'thread.social.pinterest.shares', 'thread.social.vk.shares', 'thread.social.linkedin.shares',
                'thread.social.facebook.likes', 'thread.social.facebook.shares', 'thread.social.facebook.comments',
                'thread.social.stumbledupon.shares', 'thread.site_full', 'thread.main_image', 
                'thread.site_section', 'thread.section_title', 'thread.url', 'thread.country', 'thread.title',
                'thread.performance_score', 'thread.site', 'thread.participants_count', 'thread.title_full',
                'thread.spam_score', 'thread.site_type', 'thread.published', 'thread.replies_count', 'thread.uuid',
                'external_links', 'persons', 'organizations'], axis='columns', inplace=True)

        df['locations'] = df['locations'].replace({'[]': float('nan')})
        df['locations'] = df['locations'].str.replace('[\[\]]', '', regex=True)
        print("locations done")
        df['persons'] = df['persons'].replace({'[]': float('nan')})
        df['persons'] = df['persons'].str.replace('[\[\]]', '', regex=True)
        print("persons done")
        print('saving')
        name = 'webzio_converted_json_to_csv_' + str(number)
        df.to_csv(name, index=False)