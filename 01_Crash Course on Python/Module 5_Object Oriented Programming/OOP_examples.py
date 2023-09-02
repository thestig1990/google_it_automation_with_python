print(type(0))
print(type(""))

# dir - output a list of attributes and methods that belong to the passed data type or class
print("List of attributes and methods that belong to the 'str' class:\n", dir(""))
print("List of attributes and methods that belong to the 'list' class:\n", dir([]))
print("List of attributes and methods that belong to the 'dictionaries' class:\n", dir({}))




# help - return the documentation for the corresponding class
# print("Help on class 'str':\n", help(""))
# print("Help on class 'list':\n", help([]))
# print("Help on class 'dictionaries':\n", help({}))

# help("")



# define Apple class

class Apple:
    pass


class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())

golden = Apple()
golden.color = "yellow"
golden.flavor = "soft"


print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())
