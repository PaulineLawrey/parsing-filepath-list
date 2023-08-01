import csv
import re
import os


# script written by Chat-GPT v4
INPUTFILE = './data/mjs-filepaths.csv'
OUTPUTFILE = './data/unique-folders.csv'

def get_unique_folders(input_file, output_file):
    folder_paths = {}

    with open(input_file, 'r') as in_file:
        reader = csv.DictReader(in_file)

        for row in reader:
            path = row['FolderPath']
            if path not in folder_paths:
                folder_paths[path] = len(path)

    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['FolderPath', 'Depth', 'Length', 'HasInvalidChars'])

        invalid_chars = '["*:<>?\|]'
        for path, length in folder_paths.items():
			# Calculate the folder depth
            depth = path.count(os.sep)   
                                 
            if re.search(invalid_chars, path) or path.strip() != path:
                has_invalid_chars = 'yes'
            else:
                has_invalid_chars = 'no'
            writer.writerow([path, depth, length, has_invalid_chars])

if __name__ == "__main__":
    get_unique_folders(INPUTFILE, OUTPUTFILE)
