import os
import json
import pandas as pd

class JsonToCsvConverter:
    """
    This class converts JSON files to CSV format.
    """

    def __init__(self, parent_folder):
        """
        Initialize the JsonToCsvConverter object.

        Parameters:
            parent_folder (str): The parent folder path where the JSON files are located.
        """
        self.parent_folder = parent_folder

    def _process_file(self, file_path, number):
        """
        Process an individual JSON file and convert it to a CSV file.

        Parameters:
            file_path (str): The path of the JSON file to be processed.
            number (int): A number used for generating the output CSV file name.
        """
        df = pd.DataFrame()

        with open(file_path, 'r') as f:
            contents = f.read()

        data = json.loads(contents)
        new_df = pd.json_normalize(data)

        df = pd.concat([df, new_df], ignore_index=True)

        df.drop(['ord_in_thread', 'highlightText', 'highlightTitle', 'entities.persons',
                 'entities.locations', 'entities.organizations','thread.social.gplus.shares',
                 'thread.social.pinterest.shares', 'thread.social.vk.shares', 'thread.social.linkedin.shares',
                 'thread.social.facebook.likes', 'thread.social.facebook.shares', 'thread.social.facebook.comments',
                 'thread.social.stumbledupon.shares', 'thread.site_full', 'thread.main_image',
                 'thread.site_section', 'thread.section_title', 'thread.url', 'thread.country', 'thread.title',
                 'thread.performance_score', 'thread.site', 'thread.participants_count', 'thread.title_full',
                 'thread.spam_score', 'thread.site_type', 'thread.published', 'thread.replies_count', 'thread.uuid',
                 'external_links', 'persons', 'organizations', 'uuid', 'crawled', 'locations'], axis='columns', inplace=True)

        df['persons'] = df['persons'].replace({'[]': float('nan')})
        df['persons'] = df['persons'].str.replace('[\[\]]', '', regex=True)

        name = f'webzio_converted_json_to_csv_{number}.csv'
        df.to_csv(name, index=False)

    def convert_data(self):
        """
        Convert the JSON files in the specified parent folder to CSV files.
        """
        folder_list = os.listdir(self.parent_folder)
        number = 0

        for folder in folder_list:
            folder_path = os.path.join(self.parent_folder, folder)
            file_list = os.listdir(folder_path)

            for file in file_list:
                file_path = os.path.join(folder_path, file)
                self._process_file(file_path, number)
                number += 1

        print("Conversion completed.")


# Example usage:
converter = JsonToCsvConverter(parent_folder='webz_io')
converter.convert_data()


# --------------- below is the code written using simple procedural programming ----------------------



"""import os
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
        df.to_csv(name, index=False)"""