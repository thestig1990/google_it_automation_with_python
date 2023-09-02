# Week 1 Graded Assessment

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Once you have learned the basics of a programming language, how does this affect your ability\
 to learn and use a second programming language?"

> - [ ] The syntax and semantics will be the same.
> - [x] **It’s easier to learn and use a second language.**
> - [ ] You should only code in one language.
> - [ ] It’s difficult to learn and use a second language.

### Question 2

2. Which of the following are true about programming languages? Select all that apply.

> - [x] **Similar to human language, programming languages use syntax and semantics.**
> - [x] **Programming languages are used to write computer programs and scripts.**
> - [ ] Programming languages is a synonym for pseudocode. 
> - [x] **Some common programming languages include Python, Java, C, C++, C#, and R.**

### Question 3

3. What is automation?

> - [ ] The inputs and outputs of a program
> - [x] **The process of replacing a manual step with an automated step**
> - [ ] The rules of a programming language
> - [ ] The process of designing a solution to a problem

### Question 4

4. What is the term for the set of rules for how statements are constructed in a programming language?

> - [ ] Grammar
> - [ ] Format
> - [ ] Semantics
> - [x] **Syntax**

### Question 5

5. What is a property of Python that makes it easier to understand than some other programming languages?

> - [ ] You can use Python code in any other language.
> - [ ] Python doesn’t have a defined syntax.
> - [x] **Code is similar to the English language.**
> - [ ] Basic guidelines can be given and it will write the code.

### Question 6

6. Write a Python script that outputs "Automating with Python is fun!" to the screen.\
Remember that syntax precision is important in programming languages.\
A missing capital letter, spelling error, or punctuation mark can produce errors.

```Python
# Enter code here:
print("Automating with Python is fun!")
# Should print: Automating with Python is fun!
```

### Question 7

7. What should be the output of the expression below?

```Python
print((6-2)/(5*(1+4))+3)
```

> - [ ] 5.0
> - [ ] 12.0
> - [ ] 50.0
> - [x] **3.16**

### Question 8

8. Assuming there are 60 minutes in an hour, write a program that calculates the number of minutes in a 24 hour day.\
Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.

```Python
# Enter code here:
print(24*60)

# Should print 1440
```

### Question 9

9. Mercury has a diameter of approximately 1,516 miles. Earth has a diameter of approximately 3,959 miles.\
Use Python to calculate how much larger Earth’s diameter is than Mercury's (in miles).\
 Note: Your result should be in the format of a number, not a sentence.

```Python
# Enter code here:
print(3959 - 1516)

# Should print 2443
```

### Question 10

10. Fill in the blank to calculate how many sectors a given 16 GB (gigabyte) hard disk drive has.\
The given hard drive is divided into sectors of 512 bytes each. How many sectors should this drive have?\
Your result should be in the format of just a number, not a sentence. Note: To calculate the disk size,\
multiply by multiples of 1024. In the code below, the "disk_size" of 16 GB is expressed as multiplying 16\
 by 1024 three times to get from bytes, to kilobytes, to megabytes, and finally to gigabytes.

```Python
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / sector_size


print(sector_amount) # Should print 33554432.0
```