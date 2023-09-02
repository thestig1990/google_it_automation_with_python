import re


result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada" )

print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
#print(result[3])


print(f"{result[2]} {result[1]}")

print()

# function
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

# call function
print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))


print()


# Fix the regular expression used in the rearrange_name function so that
# it can match middle names, middle initials, as well as double surnames.
# (add extra characters that we want allow in the names "." and "space")
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w* ?\w*.)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

# call function
print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))
print(rearrange_name("Hopper, Grace-Kelly M."))


print()


# add extra characters that we want allow in the names "-"(dash)
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

# call function
print(rearrange_name("Hopper, Grace M."))
print(rearrange_name("Hopper, Grace-Kelly M."))
