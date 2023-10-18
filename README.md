# parsing-filepath-list
Python scripts for parsing a file containing a list of filepaths, one per line

The list I've been working with was of the format <filepath><space><folderDepth#> but it can easily be updated to handle just filepaths (and this would be better).

The two scripts to use are:
* parse-file-list.py, and
* get-top-level-folder-stats.py

The other scripts are there to get other views of the data.
create-text-folder-tree.py isn't working, others may need to be udpated to use the 'outputs' folder rather than 'data'.

All scripts have the folder names hard-coded in constants at the top of the file.

