# Week 3 Graded Assessment

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Fill in the blanks to print the even numbers from 2 to 12.

```Python
number = 2 # Initialize the variable 
while number <= 12: # Complete the while loop condition
    print(number, end=" ")
    number += 2 # Increment the variable

# Should print 2 4 6 8 10 12 
```

### Question 2

2. Find and correct the error in the for loop. The loop should print every number from 5 to 0 in descending order.

```Python
for number in range(5, -1, -1):
    print(number)

# Should print:
# 5
# 4
# 3
# 2
# 1
# 0
```

### Question 3

3. Fill in the blanks to complete the function “even_numbers(n)”. This function should count how many\
even numbers exist in a sequence from 0 to the given “n”number, where 0 counts as an even number.\
For example, even_numbers(25)\should return 13, and even_numbers(6) should return 4.

```Python
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n:  # Complete the while loop condition
        if current_number % 2 == 0:
            current_number += 2 # Increment the appropriate variable
        count += 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1
```

### Question 4

4. Fill in the blanks to complete the “sequence” function. This function should print a sequence of numbers in descending\
order, from the given "high" variable to the given "low" variable. The range should make he loop run two times.\
Complete the range sequences in the nested loops so that the “sequence(1, 3)” function call prints the following:

3, 2, 1

3, 2, 1

```Python
def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low -1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.
```

### Question 5

5. Fill in the blanks to complete the “counter” function. This function should count down from the “start” to\
“stop”\ variables when “start” is bigger than “stop”. Otherwise, it should count up from “start” to “stop”.\
Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and\
“counter(2, 5)” will return “Counting up: 2, 3, 4, 5”..

```Python
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            start -= 1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start <= stop: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            start += 1 # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
```

### Question 6

6. Fill in the blanks to complete the “odd_numbers” function. This function should return a space-separated string\
of all odd positive numbers, up to and including the “maximum” variable that's passed into the function.\
Complete the for loop so that a function call like “odd_numbers(6)” will return the numbers “1 3 5”.

```Python
def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for odd in range(maximum+1): 

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        if odd % 2 != 0:
            return_string += str(odd) + " " 

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed
```

### Question 7

7. What happens when the Python interpreter executes a loop where a variable used inside the loop is not initialized?

> - [x] **Will produce a NameError stating the variable is not defined**
> - [ ] Nothing will happen
> - [ ] The variable will be auto-assigned a default value of 0
> - [ ] Will produce a TypeError 

### Question 8

8. What is the final value of “x” at the end of this for loop? Your answer should be only one number.

```Python
for x in range(1, 10, 3):
    print(x)
```

*Output: 7*

### Question 9

9. What number is printed at the end of this code?

```Python
num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)
```

*Output: 20*

### Question 10

10. The following code causes an infinite loop. Can you figure out what’s incorrect and how to fix it?

```Python
def count_to_ten():
  # Loop through the numbers from first to last 
  x = 1
  while x <= 10:
    print(x)
    x = 1


count_to_ten()
# Should print:
# 1
# 2
# 3 
# 4
# 5
# 6
# 7
# 8 
# 9
# 10
```

> - [x] **Variable "x" is assigned the value 1 in every loop**
> - [ ] The "x" variable is initialized using the wrong value
> - [ ] Needs to have parameters passed to the function
> - [ ] Should use a for loop instead of a while loop