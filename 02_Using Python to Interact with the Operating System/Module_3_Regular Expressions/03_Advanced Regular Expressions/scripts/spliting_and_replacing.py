import re


# using re.split module
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

# using re.split module with capturing parenthesis
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))


# using re.sub module
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

# using re.sub module to create a new string with the replacement word
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))