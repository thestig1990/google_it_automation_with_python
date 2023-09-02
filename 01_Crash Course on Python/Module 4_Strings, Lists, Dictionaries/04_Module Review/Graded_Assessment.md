# Week 4 Graded Assessment

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Fill in the blanks to complete the “confirm_length” function.\ This function should return how many characters\
a string contains as long as it has one or more characters, otherwise it will return 0. Complete the string\
operations needed in this function so that input like "Monday" will produce the output "6".

```Python
def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) > 0: 
        # Complete the return statement using a string operation.
        return len(word) 
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0
```

### Question 2

2. Complete the for loop and string method needed in this function so that a function call like\
"alpha_length("This has 1 number in it")" will return the output "17". This function should:

> 1\. accept a string through the parameters of the function;\
> 2\. iterate over the characters in the string;\
> 3\. determine if each character is a letter (counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);\
> 4\. increment the counter;\
> 5\. return the count of letters in the string.\

```Python
def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for letter in string: 
        # Complete the if-statement using a string method. 
        if letter.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21
```

### Question 3

3. Consider the following scenario about using Python lists:

A professor gave his two assistants, Jaime and Drew, the task of keeping an attendance list of students\
in the order they arrive in the classroom. Drew was the first one to note which students arrived, and then\
Jaime took over. After the class, they each entered their lists into the computer and emailed them to the professor.\
The professor wants to combine the two lists into one, in the order of each student's arrival.\
Jaime emailed a follow-up, saying that her list is in reverse order.

Complete the code to combine the two lists into one in the order of: the contents of Drew's list, followed by Jaime’s\
list in reverse order, to produce an accurate list of the students as they arrived. This function should:

> 1\. accept two lists through the function’s parameters;\
> 2\. reverse the order of “list1”;\
> 3\. combine the two lists so that “list2” comes first, followed by “list1”;\
> 4\. return the new list.\

```Python
def combine_lists(list1, list2):


  combined_list = [] # Initialize an empty list variable
  list1.reverse() # Reverse the order of "list1"
  list2.extend(list1) # Combine the two lists 
  combined_list = list2
  return combined_list  
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
```

### Question 4

4. Fill in the blank to complete the “squares” function. This function should use a list comprehension to create\
a list of squared numbers (using either the expression n*n or n**2). The function receives two variables and\
should return the list of squares that occur between the “start” and “end” variables inclusively\
(meaning the range should include both the “start” and “end” values). Complete the list comprehension\
in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”.

```Python
def squares(start, end):
    return [n**2 for n in range(start, end+1)] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Question 5

5. Fill in the blanks to complete the “countries” function. This function accepts a dictionary containing\
a list of continents (keys) and several countries from each continent (values). For each continent, format\
a string to print the names of the countries only. The values for each key should appear on their own line.

```Python
def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for continent, countries in countries_dict.items():
        # Use a string method to format the required string.
        result += "{}".format(countries) +  "\n"
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']
```

### Question 6

6. Consider the following scenario about using Python dictionaries and lists:

Tessa and Rick are hosting a party. Before they send out invitations, they want to add all of the people\
they are inviting to a dictionary so they can also add how many guests each friend is bringing to the party.

Complete the function so that it accepts a list of people, then iterates over the list and adds all of the names\
(elements) to the dictionary as keys with a starting value of 0. Tessa and Rick plan to update these values with\
the number of guests their friends will bring with them to the party. Then, print the new dictionary.

This function should:

> 1\. accept a list variable named “guest_list” through the function’s parameter;\
> 2\. add the contents of the list as keys to a new, blank dictionary;\
> 3\. assign each new key with the value 0;\
> 4\. print the new dictionary.

```Python
def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for element in guest_list: # Iterate over the elements in the list 
        result[element] = 0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}
```

### Question 7

7. Complete the function so that input like "This is a sentence." will return a dictionary that holds\
the count of each letter that occurs in the string:\
{'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.\

This function should:

> 1\. accept a string “text” variable through the function’s parameters;
> 2\. iterate over each character the input string to count the frequency of each letter found,\
(only letters should be counted, do not count blank spaces, numbers, or punctuation; keep in mind that Python is case sensitive);\
> 3\. populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter;
> 4\. return the new dictionary.

```Python
def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for letter in text.lower():   
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if letter.isalpha():
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if letter not in dictionary:  
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[letter] = 0  
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[letter] += 1  
#      ___ # Increment the letter counter. 
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
```

### Question 8

8. What do the following commands return when animal = "Hippopotamus"?

```Python
print(animal[3:6])
print(animal[-5])
print(animal[10:])
```

> - [x] **pop, t, us**
> - [ ] ppo, t, mus
> - [ ] popo, t, mus
> - [ ] ppop, o, s

### Question 9

9. What does the list "music_genres" contain after these commands are executed?

```Python
music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
```

> - [ ] ['rock', 'pop', 'blues']
> - [x] **['rock', 'pop', 'country', 'blues']**
> - [ ] ['rock', 'blues', 'country']
> - [ ] ['rock', 'blues', 'pop', 'country']

### Question 10

10. What do the following commands return?

```Python
speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]
```

> - [x] **65**
> - [ ] {"highway": 65}
> - [ ] ["highway", 65]
> - [ ] [65]