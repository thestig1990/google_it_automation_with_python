import os

# 'os.getcwd' method -  Return a unicode string representing the current working directory
print(os.getcwd())


# os.mkdir("path")  -  Create a directory.
# os.chdir("path")  -  Change the current working directory to the specified path



#os.mkdir("new_dir")
#os.rmdir("new_dir")


# 'os.listdir' method - Return a list containing the names of the files in the directory
print(os.listdir())

dir = "02_Managing Files and Directories"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    print(fullname)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")


# print(help(os.listdir))
# print(help(os.getcwd))
# print(help(os.mkdir))
# print(help(os.chdir))
print(help(os.path.join))


