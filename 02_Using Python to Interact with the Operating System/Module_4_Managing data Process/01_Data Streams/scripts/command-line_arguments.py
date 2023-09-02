# ------------------ Command-line arguments and Exit Status ------------------- #

# The list of arguments are stored in the sys module

# The Exit status - the value returned by a program to the shell
# In all Unix-like operating systems:
# 1. the exit status of the process is zero(0) when the process succeeds
# 2. and different than zero(0) if it fails


import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")

else:
    print(f"Error, the file {filename} already exists")
    sys.exit(1)