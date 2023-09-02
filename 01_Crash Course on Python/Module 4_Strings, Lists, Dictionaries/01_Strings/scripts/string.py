sentence = "It's raining cats and cats"
old = "cats"
new = "dogs"

print(sentence[-len(old):])

print(sentence[:len(old)])

print(sentence[:len(old):-1])

print(sentence[:-len(old)])