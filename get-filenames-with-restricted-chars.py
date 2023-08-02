import csv
import re

INPUTFILE = './data/mjs-filepaths.csv'
OUTPUTFILE = './data/invalid-OneDrive-filenames.csv'

def find_special_characters(filename, output_filename):
    special_chars = r'["*:<>?\|]'  # Regex pattern for special characters
    with open(filename, 'r') as input_csv, open(output_filename, 'w', newline='') as output_csv:
        reader = csv.reader(input_csv)
        writer = csv.writer(output_csv)
        next(reader)  # skip the header
        for i, row in enumerate(reader, 1):  
            if re.search(special_chars, row[0]) or row[0] != row[0].strip():
                writer.writerow([i, row[0]])

# Run the function with the name of the file you want to process
find_special_characters(INPUTFILE, OUTPUTFILE)
