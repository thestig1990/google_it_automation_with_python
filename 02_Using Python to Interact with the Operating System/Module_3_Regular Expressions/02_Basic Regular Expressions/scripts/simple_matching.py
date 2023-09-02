import re


result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)

result = re.search(r"^x", "xenon")
print(result)

result = re.search(r"p.ng", "penguin")
print(result)

result = re.search(r"p.ng", "clapping")
print(result)

result = re.search(r"p.ng", "pong")
print(result)

result = re.search(r"p.ng", "Pangaea", re.IGNORECASE)
print(result)


def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


