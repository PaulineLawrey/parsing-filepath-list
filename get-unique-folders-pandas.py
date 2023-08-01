
import pandas as pd

# script written by Chat-GPT v4
INPUTFILE = './data/mjs-filepaths.csv'
OUTPUTFILE = './data/unique-folders.txt'

def get_unique_folders(input_file, output_file):
    df = pd.read_csv(input_file)
    unique_folders = df['FolderPath'].unique()
    
    with open(output_file, 'w') as out_file:
        for path in unique_folders:
            out_file.write(f"{path}\n")

if __name__ == "__main__":
    get_unique_folders(INPUTFILE, OUTPUTFILE)
