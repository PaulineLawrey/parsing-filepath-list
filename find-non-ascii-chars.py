def find_non_ascii_lines(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, 1):
            if not line.isascii():
                print(f"Line {i} contains non-ASCII characters: {line.strip()}")

# Run the function with the name of the file you want to process
find_non_ascii_lines('./pml-output.txt')
