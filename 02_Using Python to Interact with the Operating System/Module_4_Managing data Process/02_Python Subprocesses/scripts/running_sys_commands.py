#!/usr/bin/env python3
# --------------------- Running System Commands in Python --------------------- #

# To successfully execute the script, run it from bash terminal or in the 
# WSL(Windows Subsystem for Linux) 
# Example:
# $ python running_sys_commands.py
# Sat, Jul  8, 2023  9:13:05 AM
# CompletedProcess(args=['date'], returncode=0)


# Subprocess module provides a way to execute system commands!!!

import subprocess


# sleeps for 5 seconds before executing the next line of code
# subprocess.run(["sleep", "5"])
count = 5
while count >=0:
    subprocess.run(["sleep", "1"])
    print(f"...{count}")
    count -= 1

# NOTICE!!!!!!!!:
# while sleep command was running the interpreter was blocked and we couldn't interact with it.
    

print(subprocess.run(["date"]))

# print(help(subprocess))
# print(help(subprocess.run))

result = subprocess.run(["ls", "this_file_not_exist"])
print(f"return code of the process 'subprocess.run(['ls', 'this_file_not_exist'])': {result.returncode}")


# A system command that sends ICMP packets can be executed within a script by using which of the following?

# 1. subprocess.run   <---  RIGHT!!!!
# 2. Ping
# 3. CompletedProcess
# 4. Arguments

# Correct
# Right on! This function will execute a system command such as ping.