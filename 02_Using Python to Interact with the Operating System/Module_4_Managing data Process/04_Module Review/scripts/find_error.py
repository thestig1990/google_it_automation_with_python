#!/usr/bin/env python3

# The sys module provides information about the Python interpreter's constants, functions, and methods.
# The os module provides a portable way of using operating system dependent functionality with Python.
# Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# We can use regular expressions using re module.

import sys
import os
import re


# In this lab, we'll search for the CRON error that failed to start. To do this, we'll use a python script
# to search log files for a particular type of ERROR log. In this case, we'll search for a CRON error within
# the fishy.log file that failed to start by narrowing our search to "CRON ERROR Failed to start".


# Now, write a function error_search that takes log_file as a parameter and returns returned_errors.
# Define the error_search function and pass the log file to it as a parameter:
def error_search(log_file):
    # Define an input function to receive the type of ERROR that the end-user
    # would like to search and assign to a variable named error
    error = input("What is the error? ")
    returned_errors = []
    # Use the Python file's handling methods to open the log file in reading mode
    # and use 'UTF-8' encoding.
    with open(log_file, 'r', encoding='UTF-8') as file:
        for log in file.readlines():
            # create a list to store all the patterns (user input) that will be searched
            # and, initially it has a pattern "error" to filter out all the ERROR logs only
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            # print([re.search(error_pattern, log.lower()) for error_pattern in error_patterns])
            # Now, let's use the search() method (present in re module) to check whether the file fishy.log
            # has the user defined pattern and, if it is available, append them to the list returned_errors.
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        # Next, close the file fishy.log and return the results stored in the list 
        file.close()
    return returned_errors


# Let's define another function file_output that takes returned_errors,
# returned by a previous function, as a formal parameter.
def file_output(returned_errors):
    # Using Python file handling methods, write returned_errors into the
    # errors_found.log file by opening the file in writing mode
    # Use the method os.path.expanduser ('~'), which returns the home directory of your system instance
    # Then, we'll concatenate this path (to the home directory) to the file errors_found.log in /data directory
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


# Now, let's call the functions and run the script.
# Define the main function and call both functions that we defined in the earlier sections.
if __name__ == "__main__":
    # The variable log_file takes in the path to the log file passed as a parameter.
    # In our case, the file is fishy.log
    log_file = sys.argv[1]
    # Call the first function i.e., error_search() and pass the variable log_file
    # to the function. This function will search and return a list of errors that
    # would be stored in the variable returned_errors
    returned_errors = error_search(log_file)
    # Call the second function file_output and pass the variable returned_errors
    # as a parameter
    file_output(returned_errors)
    # sys.exit(0) is used to exit from Python, the optional argument passed can be
    # an integer giving the exit status (defaulting to zero), or another type of object.
    # If it is an integer, zero is considered "successful termination" and any nonzero
    # value is considered an "abnormal termination" by shells
    sys.exit(0)
