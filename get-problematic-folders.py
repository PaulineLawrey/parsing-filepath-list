import csv
import os

INPUTFILE = './data/mjs-filepaths.csv'
OUTPUTFILE = './data/folder-levels.csv'

def process_file(input_file, output_file):
    unique_rows = set()

    with open(input_file, 'r') as in_file:
        reader = csv.DictReader(in_file)

        for row in reader:
            if int(row['PathLength']) > 200:
                # Split the folder path into individual folders, up to a maximum of 5
                folders = row['FolderPath'].split(os.sep)[:5]
                
				# Pad with empty strings to always have 5 levels
                folders += [''] * (5 - len(folders))

                # Create a key for unique checking
                unique_key = '/'.join(folders)

                # Add the tuple to the set of unique rows
                unique_rows.add((unique_key, *folders))

    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)

        # Write the header row
        writer.writerow(['UniqueKey', 'Level1', 'Level2', 'Level3', 'Level4', 'Level5'])

        # Write the unique rows to the CSV file
        for unique_key, level1, level2, level3, level4, level5 in unique_rows:
            writer.writerow([unique_key, level1, level2, level3, level4, level5])

if __name__ == "__main__":
    process_file(INPUTFILE, OUTPUTFILE)
