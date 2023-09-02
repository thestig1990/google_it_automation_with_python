file = open("01_Reading and Writing Files\spider.txt", "r") # "r" - read only mode
print(file.readline())

print(file.read())

file.close()

print()

with open("01_Reading and Writing Files\spider.txt", "r") as file:
    print(file.readline())