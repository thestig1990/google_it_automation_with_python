with open("01_Reading and Writing Files\\novel.txt", "w") as file: # "w" - write only mode
    file.write("It was a dark and stormy night\n")


with open("01_Reading and Writing Files\\novel.txt", "a") as file: # "a" - append at the end of the file
    file.write("It was a dark and stormy night\n")


with open("01_Reading and Writing Files\\novel.txt", "r+") as file: # "r+" - read-write mode
    file.write("It was a dark and stormy night")
