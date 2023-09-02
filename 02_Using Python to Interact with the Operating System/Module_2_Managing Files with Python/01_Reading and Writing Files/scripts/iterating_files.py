with open("01_Reading and Writing Files\spider.txt", "r") as file:
    for line in file:
        print(line.upper())

print("\n")

with open("01_Reading and Writing Files\spider.txt", "r") as file:
    for line in file:
        print(line.upper(), end="")

print("\n")

with open("01_Reading and Writing Files\spider.txt", "r") as file:
    for line in file:
        print(line.strip().upper())



file = open("01_Reading and Writing Files\spider.txt", "r")
lines = file.readlines()
file.close()

print(lines)
lines.sort()
print([line[:-1] for line in lines])


