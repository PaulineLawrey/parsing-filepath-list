#!/bin/bash

# Check for valid input
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 /path/to/search"
    exit 1
fi

SEARCH_DIR="$1"

# Ensure the search directory does not end with a slash
SEARCH_DIR="${SEARCH_DIR%/}"

# Search for folders and files containing the specified characters
find "$SEARCH_DIR" -mindepth 1 -type f -o -type d | grep -E "[:\*<>?|]"

exit 0
