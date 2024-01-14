import pandas as pd
import os

class DataConverter:
    """
    This class converts data from multiple files into a consolidated CSV file format.
    """

    def __init__(self, data_directory, chunk_size=800):
        """
        Initialize the DataConverter object.

        Parameters:
            data_directory (str): The directory path where the data files are located.
            chunk_size (int): The number of files to process in each iteration. Default is 800.
        """
        self.data_directory = data_directory
        self.chunk_size = chunk_size

    def _process_file(self, file_path):
        """
        Process an individual file and extract relevant information.

        Parameters:
            file_path (str): The path of the file to be processed.

        Returns:
            list: A list containing the extracted information from the file.
        """
        lines = []
        final_list = []

        if file_path == 'ReutersNews106521/20131120/153.tar.gz':
            return []

        with open(file_path, 'r') as f:
            for line in f:
                if line.strip() != '':
                    lines.append(line.strip('\n'))

        if len(lines) != 6:
            return []

        new_index = None
        for i in range(5, len(lines)):
            if lines[i][0] == ' ':
                new_index = i
                break

        for i in range(0, 4):
            final_list.append(lines[i].strip('--'))

        if new_index is not None:
            short_text = ' '.join(lines[4:new_index])
            long_text = ' '.join(lines[new_index:])
            final_list.append(short_text)
            final_list.append(long_text)
        else:
            long_text = ' '.join(lines[5:])
            final_list.append(long_text)

        return final_list

    def convert_data(self):
        """
        Convert the data from multiple files into a consolidated CSV file.
        """
        all_list = []
        folder_list = os.listdir(self.data_directory)
        previous = self.chunk_size

        for i in range(self.chunk_size, len(folder_list), self.chunk_size):
            if i == self.chunk_size:
                continue
            smaller_list = folder_list[previous:i]

            for folder in smaller_list:
                folder_name = os.path.join(self.data_directory, str(folder))
                file_list = os.listdir(folder_name)

                for file in file_list:
                    file_path = os.path.join(folder_name, file)
                    extracted_data = self._process_file(file_path)
                    if extracted_data:
                        all_list.append(extracted_data)

            df = pd.DataFrame(all_list, columns=['Title', 'Authors', 'Date', 'Url', 'Abstract', 'News'])
            name = f'ReutersNews106521_{str(smaller_list[0])}_{str(smaller_list[-1])}.csv'
            df.to_csv(name, index=False)

            previous = i

        print("Conversion completed.")


# Example usage:
converter = DataConverter(data_directory='ReutersNews106521', chunk_size=800)
converter.convert_data()



# --------------- below is the code written using simple procedural programming ----------------------
'''

import pandas as pd
import os

def convert(smaller_list):
    all_list = []
    new_list = smaller_list

    for folder in new_list:
        folder_name = 'ReutersNews106521/' + str(folder)
        file_list = os.listdir(folder_name)
        for file in file_list:
            file_path = os.path.join(folder_name, file)
            lines = read_lines(file_path)
            if len(lines) != 6:
                break
            final_list = process_lines(lines)
            all_list.append(final_list)

    df = pd.DataFrame(all_list, columns =['Title', 'Authors', 'Date', 'Url', 'Abstract', 'News'])
    name = 'ReutersNews106521_' + str(new_list[0]) + "_" + str(new_list[-1]) + '.csv'
    df.to_csv(name, index=False)

def read_lines(file_path):
    lines = []
    if file_path == 'ReutersNews106521/20131120/153.tar.gz':
        return lines
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip() != '':
                lines.append(line.strip('\n'))
    return lines

def process_lines(lines):
    final_list = []
    for i in range(0, 4):
        final_list.append(lines[i].strip('--'))
    new_index = find_new_index(lines)
    if new_index != None:
        short_text = ' '.join(lines[4:new_index])
        long_text = ' '.join(lines[new_index:len(lines)])
        final_list.append(short_text)
        final_list.append(long_text)
    else:
        long_text = ' '.join(lines[5:len(lines)])
        final_list.append(long_text)
    return final_list

def find_new_index(lines):
    for i in range(5,len(lines)):
        if lines[i][0] == ' ':
            return i
    return None



folder_list = os.listdir('ReutersNews106521')
previous = 800
for i in range(800, len(folder_list), 800):
    if i == 800:
        continue
    smaller_list = folder_list[previous:i]
    convert(smaller_list)
    previous = i
    print("Done ", str(i))

'''


# --------------- below is the original start code written ----------------------
'''
import pandas as pd
import os

def convert(smaller_list):
    all_list = []
    new_list = smaller_list

    for folder in new_list:
        folder_name = 'ReutersNews106521/' + str(folder)
        file_list = os.listdir(folder_name)
        for file in file_list:
            file_path = os.path.join(folder_name, file)

            lines = []
            final_list = []
            if file_path == 'ReutersNews106521/20131120/153.tar.gz':
                continue
            with open(file_path, 'r') as f:
                for line in f:
                    if line.strip() != '':
                        lines.append(line.strip('\n'))
            if len(lines) != 6:
                break
            new_index = None
            for i in range(5,len(lines)):
                if lines[i][0] == ' ':
                    new_index = i
                    break
            for i in range(0, 4):
                final_list.append(lines[i].strip('--'))
            if new_index != None:
                short_text = ' '.join(lines[4:new_index])
                long_text = ' '.join(lines[new_index:len(lines)])
                final_list.append(short_text)
                final_list.append(long_text)
            else:
                long_text = ' '.join(lines[5:len(lines)])
                final_list.append(long_text)
            all_list.append(final_list)

    df = pd.DataFrame(all_list, columns =['Title', 'Authors', 'Date', 'Url', 'Abstract', 'News'])
    name = 'ReutersNews106521_' + str(new_list[0]) + "_" + str(new_list[-1]) + '.csv'
    df.to_csv(name, index=False)



folder_list = os.listdir('ReutersNews106521')
previous = 800
for i in range(800, len(folder_list), 800):
    if i == 800:
        continue
    smaller_list = folder_list[previous:i]
    convert(smaller_list)
    previous = i
    print("Done ", str(i))

'''