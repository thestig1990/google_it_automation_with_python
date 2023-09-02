import os


# file = open("C:\\Users\Yevhen Yakymov\AppData\Local\Programs\Python\Python310\Lib\\ntpath.py", "r")
# for line in file:
#     print(line)
# file.close()

os.remove("novel.txt")

os.rename("novel_copy.txt", "novel.txt")

print(os.path.exists("novel.txt"))
print(os.path.exists("novel_copy.txt"))
