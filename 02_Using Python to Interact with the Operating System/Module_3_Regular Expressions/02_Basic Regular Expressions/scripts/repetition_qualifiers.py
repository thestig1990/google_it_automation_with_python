import re


result = re.search(r"Py.*n", "Pygmalion")
print(result)

result = re.search(r"Py.*n", "Python Programming")
print(result)

result = re.search(r"Py[a-z]*n", "Python Programming")
print(result)

result = re.search(r"Py[a-z]*n", "Python Programming")
print(result)

result = re.search(r"Py[a-z]*n", "Pyn")
print(result)


result = re.search(r"o+l+", "goldfish")
print(result)

result = re.search(r"o+l+", "woolly")
print(result)

result = re.search(r"o+l+", "boil")
print(result)


# The repeating_letter_a function checks if the text passed includes the letter "a"
# (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana")
# is True, while repeating_letter_a("pineapple")is False. Fill in the code to make this work. 
def repeating_letter_a(text):
  result = re.search(r".*a.*a.*", text, re.IGNORECASE)
  return result != None
  #return bool(result)

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

# my realization
# def repeating_letter_a(text):
#   result = re.findall(r"a", text, re.IGNORECASE)
#   if len(result) > 1:
#       return result != None
#   else:
#       return False

# print(repeating_letter_a("banana")) # True
# print(repeating_letter_a("pineapple")) # False
# print(repeating_letter_a("Animal Kingdom")) # True
# print(repeating_letter_a("A is for apple")) # True



result = re.search(r"p?each", "To each their own")
print(result)

result = re.search(r"p?each", "I like peaches")
print(result)
