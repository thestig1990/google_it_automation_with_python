#!/usr/bin/env python3
# ---------------------- Advanced Subprocess Management ---------------------- #

# To successfully execute the script, run it from bash terminal or in the 
# WSL(Windows Subsystem for Linux) 
# Example:
# $ python3 advanced_subprocess_managment.py

import os
import subprocess


# calling the copy method of the OS environment dictionary that contains
# the current environment variables. This creates a new dictionary that we 
# can change as needed without modifying the original environment.
my_env = os.environ.copy()
print(f"env  --->  {my_env}")
print()

# Adding one extra directory to the PATH variable
# NOTICE: PATH variable indicate where the OS will look for the executable programs!

# We're calling the join method on the OS path substring.
# This join elements of the list that we're passing with a path separator corresponding.
# So here we're joining /opt/my_app and the old value of the path variable to the path separator.
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
print(f"env  --->  {my_env}")
print()

# Finally, we call the my_app command, setting the end parametr to the new environment
# that we have just prepared.
try:
    result = subprocess.run(["myapp"], env=my_env)   
except FileNotFoundError:
    print("No such file or directory.")
else:
    print(f"return code of the process - {result.returncode}")