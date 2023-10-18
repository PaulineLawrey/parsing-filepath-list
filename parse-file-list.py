import csv
import os
import re
import pandas as pd

# script further modified by Chat-GPT v4
INPUTFILE = './raw-data/pml-output.txt'
OUTPUTFILE = './outputs/mjs-filepaths.csv'

def process_file(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)

        # Write the header row
        writer.writerow(['OriginalFilePath', 'PathLength', 'FolderPath', 'TopFolder', 'FolderDepth', 'IsInvalidFoldername', 'IsInvalidFilename', 'Extension'])

        for line in in_file:
            
            line = line[2:]    # Strip './' from the start of each string
            # Strip trailing newlines and split at the last space character
            line = line.rstrip('\n')
            last_space_index = line.rfind(' ')

            if last_space_index == -1:
                # No space found, so put the entire line in the first column
                writer.writerow([line, '', '', '', '', '', ''])
            else:
                # Split the line into two parts
                first_part = line[:last_space_index]
                second_part = line[last_space_index + 1:]

                # Extract the path without the filename or extension
                path_without_filename = os.path.dirname(first_part)

                # Calculate the folder depth
                if (path_without_filename == ''):
                    folder_depth = 0
                else:
                    folder_depth = path_without_filename.count(os.sep) + 1
                top_folder = path_without_filename.split(os.sep)[0]

                # Check for invalid filename
                filename = os.path.basename(first_part)
                invalid_chars = '["*:<>?/\\|]'
                if re.search(invalid_chars, filename) or filename.strip() != filename:
                    invalid_filename = 'yes'
                else:
                    invalid_filename = 'no'

                # Check for invalid folder name
                foldername = os.path.basename(path_without_filename)
                if re.search(invalid_chars, foldername) or foldername.strip() != foldername:
                    invalid_foldername = 'yes'
                else:
                    invalid_foldername = 'no'

                # Extract file extension
                extension = os.path.splitext(first_part)[1][1:]

                # Write the parts to the CSV file
                writer.writerow([first_part, len(first_part) + 1, path_without_filename, top_folder, folder_depth, invalid_foldername, invalid_filename, extension])

if __name__ == "__main__":
    process_file(INPUTFILE, OUTPUTFILE)
