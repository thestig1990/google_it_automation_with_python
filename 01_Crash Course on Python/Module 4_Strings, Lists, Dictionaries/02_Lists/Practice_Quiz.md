# Practice Quiz: Lists

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Given a list of filenames, we want to rename all the files with extension hpp to the extension h.\
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.\
Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

```Python
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = [filename.replace("hpp", "h") if filename[-3:] == "hpp" else filename for filename in filenames]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
```

*Great work! You're starting to see the benefits of knowing how to operate with lists and strings.*

### Question 2

2. Let's create a function that turns text into pig latin: a simple text transformation that modifies each\
word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

```Python
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  pig_latin_words = []
  for word in words:
    # Create the pig latin word and add it to the list
    pig_latin_words.append(word[1:] + word[0] + "ay")
    # Turn the list back into a phrase
  return " ".join(pig_latin_words)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
```

*Nice! You're using some of the best string and list functions to make this work. Great job!*

### Question 3

3. Which list method can be used to add a new element to a list at a specified index position?

> - [ ] list.pop(index)
> - [x] **list.insert(index, x)**
> - [ ] list.add(index, x)
> - [ ] list.append(x)

*The list.insert(index, x) method will insert the given “x” element into the list at the specified index position.*

### Question 4

4. Tuples and lists are very similar types of sequences. What is the main thing that makes a tuple different from a list?"

> - [ ] A tuple is mutable
> - [ ] A tuple contains only numeric characters
> - [ ] **A tuple is immutable**
> - [ ] A tuple can contain only one type of data at a time

*Awesome! Unlike lists, tuples are immutable, meaning they can't be changed.*

### Question 5

5. The group_list function accepts a group name and a list of members, and returns a string with the format:\
group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".\
Fill in the gaps in this function to do that.

```Python
def group_list(group, users):
  members = group + ": " + ", ".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
```

*Nice job! You're doing well, working with list elements!*

### Question 6

6. The guest_list function reads in a list of tuples with the name, age, and profession of each party guest,\
and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"),\
("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef.\
Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer.\
Fill in the gaps in this function to do that.

```Python
def guest_list(guests):
	for guest in guests:
		name, age, prof =  guest
		print("{} is {} years old and works as {}".format(name, age, prof))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
```

*Well done! See how the format methodology combines with tuple functionality to easily create interesting code!*