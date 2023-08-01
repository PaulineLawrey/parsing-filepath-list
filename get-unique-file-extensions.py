import csv
import os

def find_unique_extensions(filename):
    extensions = set()
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ext = os.path.splitext(row[0])[1]
            extensions.add(ext)
    return sorted(extensions)

# Run the function with the name of the file you want to process
unique_extensions = find_unique_extensions('./mjs-filepaths.csv')

print("Unique file extensions:")
for ext in unique_extensions:
    print(ext)

