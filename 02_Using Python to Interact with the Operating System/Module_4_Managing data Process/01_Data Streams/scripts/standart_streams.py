# -------------------------------- I/O streams -------------------------------- #

# The basic  mechanism for performing input and output operations in your programs

# I/O streams:
# 1. standart input - STDIN
# 2. standart output - STDOUT
# 3. standart error - STDERR


# example 1
data = input("This will come frome STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)  # ---> TypeError