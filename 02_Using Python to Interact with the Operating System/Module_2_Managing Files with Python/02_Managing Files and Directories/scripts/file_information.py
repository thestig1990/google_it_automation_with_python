import os
import datetime


# os.path.getsize method - Return the size of a file
print("The size of the 'novel.txt' file is {} bytes".format(os.path.getsize("novel.txt")))

print()

# os.path.getmtime method - Return the last modification time of a file
timestamp = os.path.getmtime("novel.txt")
print("Time of the last modification of the file 'novel.txt' - {}".format(datetime.datetime.fromtimestamp(timestamp)))

print()

# os.path.isfile method - Test whether a path is a regular file
file = "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print("Is a {} regular file? - {}".format(file, os.path.isfile(file)))
    print(f"File '{file}' not found", end="\n")

print()

# os.path.abspath method - Return the absolute version of a path
print("The absolute path of the file 'novel.txt' - {}".format(os.path.abspath("novel.txt")))



# print(help(os.path.isfile))
# print(help(os.path.getsize))
# print(help(os.path.getmtime))
# print(help(os.path.abspath))

