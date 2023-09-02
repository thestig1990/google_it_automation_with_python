import re


result = re.search(r"[a-zA-Z]{5}", "a ghost")
print(result)


result = re.search(r"[a-zA-Z]{5}", "a scarry ghost appeared")
print(result)


result = re.findall(r"[a-zA-Z]{5}", "A scary ghost appeared")
print(result)


result = re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")
print(result)


result = re.findall(r"\w{5,10}", "I really like strawberries")
print(result)


result = re.findall(r"\w{5,}", "I really like strawberries")
print(result)


result = re.findall(r"s\w{,20}", "I really like strawberries")
print(result)


# The long_words function returns all words that are at least 7 characters.
# Fill in the regular expression to complete this function.
def long_words(text):
  pattern = "\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []