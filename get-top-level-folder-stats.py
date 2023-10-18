import re
import os
import pandas as pd

INPUTFILE = 'outputs/mjs-filepaths.csv'
OUTPUTFILE = 'outputs/folder-stats.csv'

import pandas as pd

# Function to filter strings based on the pattern
def filter_strings(strings_list):
    return list(set(s for sublist in strings_list for s in sublist if pattern.search(s)))

def count_strings(strings_list):
    filtered = [s for sublist in strings_list for s in sublist if pattern.search(s)]
    return len(set(filtered))

def get_file_count(rows):
    return rows.count()

df = pd.read_csv(INPUTFILE, true_values=['yes'], false_values=['no'])
df = df[df['FolderPath'].notna()]

df['SubFolders'] = df['FolderPath'].str.split(os.sep)

pattern = re.compile(r'["*:<>?\\|\[\],]|(^\s)|(\s$)')
new_df = df.groupby('TopFolder').agg({ 
	"FolderDepth": max,
    'SubFolders': [count_strings, filter_strings],
    "FolderPath": get_file_count,
	"IsInvalidFilename": sum,
}).reset_index()

new_df.columns = ['TopFolder', 'MaxFolderDepth', 'NumProbFolders', 'ProbFolders', 'NumFiles', 'NumProbFiles']
# print(new_df.columns())
print(new_df)
new_df.to_csv(OUTPUTFILE, index=False)
