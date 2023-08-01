""" 
Generated by ChatGPT v4
Input prompt:
	Write a python script that will read in a csv file with the columns ['OriginalFilePath', 'PathLength', 'FolderPath', 'FolderDepth', 'IsInvalidFoldername', 'IsInvalidFilename'] and generates a text file that shows the folder tree structure for the paths that start with a path given as an argument. There is an optional argument that limits the depth of the folder structure to document. There is an optional argument that limits the rows to be included to ones that have PathLength greater it.
"""
import csv
import sys
import os

INPUTFILE = './data/mjs-filepaths.csv'
OUTPUTFILE = './data/folder-tree.txt'

def generate_tree(input_file, output_file, root_path, max_depth=None, min_length=None):
    paths = set()

    with open(input_file, 'r') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            path = row['FolderPath']
            if path.startswith(root_path) and (min_length is None or int(row['PathLength']) > min_length):
                paths.add(path)

    with open(output_file, 'w') as out_file:
        for path in sorted(paths):
            depth = path.count(os.sep) - root_path.count(os.sep)
            if max_depth is not None and depth > max_depth:
                continue

            indent = '  ' * depth
            out_file.write(f"{indent}{os.path.basename(path)}\n")

if __name__ == "__main__":
    root_path = sys.argv[1] if len(sys.argv) > 1 else ''
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else None
    min_length = int(sys.argv[3]) if len(sys.argv) > 3 else None

    generate_tree(INPUTFILE, OUTPUTFILE, root_path, max_depth, min_length)
