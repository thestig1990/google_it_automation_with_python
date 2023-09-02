# Practice Quiz: For Loops

*Congratulations! You passed! Grade received 100%*

### Question 1

1. How are while loops and for loops different in Python?

> - [ ] While loops can be used with all data types, for loops can only be used with numbers.
> - [ ] For loops can be nested, but while loops can't.
> - [x] **While loops iterate while a condition is true, for loops iterate through a sequence of elements.**
> - [ ] While loops can be interrupted using break, for loops using continue.

*You got it! We can use while loops when we want our code to execute repeatedly while a condition is true,*\
*and for loops when we want to execute a block of code for each element of a sequence.*

### Question 2

2. Which option would fix this for loop to print the numbers 12, 18, 24, 30, 36?

```Python
for n in range(6,18,3):
    print(n*2)
```

> - [ ] .

```Python
 for n in range(6,18,3):
    print(n+2)
```

> - [x] .

```Python
for n in range(6,18+1,3):
    print(n*2)
```

> - [ ] .

```Python
 for n in range(12,36,6):
    print(n*2)
```

> - [ ] .

```Python
for n in range(0,36+1,6):
    print(n)
```

*Great job! To include 18 in the range, add 1 to it. The second parameter could be written as 18+1 or 19.*

### Question 3

3. Which for loops will print all even numbers from 0 to 18? Select all that apply.

> - [x] .

```Python
for n in range(19):
    if n % 2 == 0:
        print(n)
```

> - [ ] .

```Python
for n in range(18+1):
    print(n**2)
```

> - [ ] .

```Python
for n in range(0,18+1,2):
    print(n*2)
```

> - [ ] .

```Python
for n in range(10):
    print(n+n)
```

*Correct! This loop will print all even numbers from 0 to 18. The range of “n” will start at 0 and end at 18*\
*(the end range value of 19 is excluded). The variable  “n” will increment by the default of 1 in each iteration of the loop.*\
*The if statement uses the modulo operator to test if the "n" variable is divisible by 2. If True, the if statement will print*\
*the value of "n" and exit back into the for loop for the next iteration of "n".*

### Question 4

4. Fill in the blanks so that the for loop will print the first 10 cube numbers (x**3) in a range\
 that starts with x=1 and ends with x=10.

```Python
for x in range(1,10+1):
  print(x**3)
```

*You nailed it! You got the code to print the first 10 cubes.*

### Question 5

5. Write a for loop with a three parameter range() function that prints the multiples of 7 between 0 and 100.\
Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

```Python
for x in range(0,100,1):
  if x == 0 or x % 7 == 0:
    print(x)
```

*Awesome! You're getting Python to do all the work for you.*