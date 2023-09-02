import re


result = re.search(r"[Pp]ython", "Python")
print(result)


result = re.search(r"[a-z]way", "The end of the highway")
print(result)


result = re.search(r"[a-z]way", "What a way to go")   # None
print(result)


result = re.search(r"cloud[a-zA-Z0-9]", "cloudy")
print(result)

result = re.search(r"cloud[a-zA-Z0-9]", "cloud9")
print(result)

result = re.search(r"cloud[a-zA-Z0-9]", "cloudY")
print(result)


result = re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")
print(result)

result = re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")
print(result)


result = re.search(r"cat|dog", "I like cats.")
print(result)

result = re.search(r"cat|dog", "I like dogs.")
print(result)

result = re.search(r"cat|dog", "I like both dogs and cats.")
print(result)

result = re.findall(r"cat|dog", "I like both dogs and cats.")
print(result)