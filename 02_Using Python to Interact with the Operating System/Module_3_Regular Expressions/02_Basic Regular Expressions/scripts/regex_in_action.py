import re

match = re.search(r"A.*a", "Argentina")
print(match)
print("Match =", match.group())

match = re.search(r"A.*a", "Azerbaijan")
print(match)
print("Match =", match.group())

match = re.search(r"^A.*a$", "Azerbaijan")
print("Match =", match)

match = re.search(r"^A.*a$", "Australia")
print(match)
print("Match =", match.group())


# checking the correctness of the variable name:
# 1:
var_match = re.search(r"^\D\w+$", "_var_1")
print(var_match)
print(f"'{var_match.group()}' is a valid variable" if var_match else None)

# 2:
var_match = re.search(r"^[a-zA-z_][a-zA-Z0-9_]*$", "var_first_")
print(var_match)
print(f"'{var_match.group()}' is a valid variable" if var_match else None)



# Fill in the code to check if the text passed looks like a standard sentence,
# meaning that it starts with an uppercase letter, followed by at least some
# lowercase letters or a space, and ends with a period, question mark, or exclamation point. 

def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ]+[.?!]$", text)
    return result != None
    # return bool(result)
  

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True