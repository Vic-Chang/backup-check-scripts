# Introduction

This code is a Python script designed to compare the files in two given folders and output two text files. One text file contains a list of changed files between the two folders, and the other text file contains a list of files that exist in the source folder but not in the target folder.

# Usage

To use this script, open a terminal and navigate to the directory containing the script. Then, enter the following command:

``` bash
python script.py <source folder> <target folder>
```

Replace <source folder> with the path to the folder you want to compare from, and <target folder> with the path to the folder you want to compare to.

For example:

``` bash
python script.py ./Documents/old_folder ./Documents/new_folder
```

# Output

The script will output two text files:

* `backup_change_list.txt`: contains a list of changed files between the two folders.

* `Un_Backup_List.txt`: contains a list of files that exist in the source folder but not in the target folder.
