#!/bin/bash

# Create the text file oldFiles.txt
> oldFiles.txt

# Search for all lines that contain the name "jane" and save the file names into a variable
files=$(grep ' jane ' ../data/list.txt | cut -d ' ' -f 3)

# Create path of the HOME directory
home_path=$HOME

# Iterate over the files variable and add a test expression within the loop.
# If the item within the files variable passes the test, add/append it to the file oldFiles.txt
for file in $files; do
    if test -e $home_path$file; then
        echo $home_path$file >> oldFiles.txt
    fi
done
