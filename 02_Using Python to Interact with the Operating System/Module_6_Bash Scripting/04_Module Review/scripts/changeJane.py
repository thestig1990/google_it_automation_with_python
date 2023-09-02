#!/usr/bin/env python3


import sys
import subprocess

# The sys (System-specific parameters and functions) module provides access to some variables
# used or maintained by the interpreter and to functions that interact with the interpreter.

# The subprocess module allows you to spawn new processes, connect to their
# input/output/error pipes, and get their return codes.

# Since oldFiles.txt is passed as a command line argument, it's stored in the variable sys.argv[1]
file = sys.argv[1]

# Open the file from the first argument to read its contents using open() method and with block
with open(file, "r") as f:
    # traverse each line in the file using readlines() method
    for line in f.readlines():
        # Use line.strip() to remove any whitespaces or newlines and fetch the old name.
        source = line.strip()
        # Once we have the old name, use replace() function to replace "jane" with "jdoe"
        destination = source.replace("jane", "jdoe")
        # Invoke a subprocess by calling run() function. This function takes arguments used to launch the process.
        # These arguments may be a list or a string. In this case, we should pass a list consisting of the command
        # to be executed, followed by arguments to the command.
        subprocess.run(["mv", source, destination])
    # Close the file that was opened at the beginning.
    f.close()
