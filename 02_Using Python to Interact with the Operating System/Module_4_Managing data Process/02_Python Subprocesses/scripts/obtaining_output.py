#!/usr/bin/env python3
# ------------------ Obtaining the Output of a System Command ------------------ #

# To successfully execute the script, run it from bash terminal or in the 
# WSL(Windows Subsystem for Linux) 
# Example:
# $ python3 obtaining_output.py


# Heads up! This example uses the capture_output parameter of subprocess.run,
# which was introduced in Python 3.7. Please make sure you are running
# Python 3.7 or later to follow along !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# In Linux host command can convert a host name to an IP address and vice versa!
# Parameter capture_output=True


import subprocess


result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(f"return code of the process 'subprocess.run(['host', '8.8.8.8'], capture_output=True)': {result.returncode}")
print(f"STDOUT: {result.stdout}")
print()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# Encoding specifications(like UTF-8) indicate which sequences of bytes represent which characters.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# If we want that array of bytes to become a proper string we can call 'decode method'!
# This method applies an encoding to transform the bytes into a string.

print(f"STDOUT: {result.stdout.decode()}")
print(f"STDOUT: {result.stdout.decode().split()}")
print()



# stderr example:

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(f"return code of the process 'subprocess.run(['rm', 'does_not_exist'], capture_output=True)': {result.returncode}")
print(f"STDERR: {result.stderr}")
print(f"STDERR: {result.stderr.decode()}")