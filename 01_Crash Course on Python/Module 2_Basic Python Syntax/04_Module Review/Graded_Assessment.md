# Week 2 Graded Assessment

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Complete the code to output the statement, “Marjery lives at her home address of 1234 Mockingbird Lane”.\
 Remember that precise syntax must be used to receive credit.

```Python
name = "Marjery"
home_address = "1234 Mockingbird Lane"
print(name + " lives at her home address of " + home_address)
# Should print "Marjery lives at her home address of 1234 Mockingbird Lane"
```

### Question 2

2. What's the value of this Python expression: "big" > "small"?

> - [ ] True
> - [x] **False**
> - [ ] big
> - [ ] small

### Question 3

3. What is the elif keyword used for?

> - [ ] To mark the end of the if statement
> - [x] **To handle more than two comparison cases**
> - [ ] To replace the "or" clause in the if statement
> - [ ] Nothing - it's a misspelling of the else-if keyword

### Question 4

4. Consider the following scenario about using if-elif-else statements:

Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass".\
For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score".

Fill in the blanks in this function so that it returns the appropriate "Pass", "Fail", or "Top Score" grade.

```Python
def exam_grade(score):
    if 95 < score <= 100:
        grade = "Top Score"
    elif 60 <= score <= 95:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

print(exam_grade(65)) # Should print Pass
print(exam_grade(55)) # Should print Fail
print(exam_grade(60)) # Should print Pass
print(exam_grade(95)) # Should print Pass
print(exam_grade(100)) # Should print Top Score
print(exam_grade(0)) # Should print Fail
```

### Question 5

5. What's the value of the comparison in this if statement? Hint: The answer is not what the code will print.

```Python
n = 4
if n*6 > n**2 or n%2 == 0:
    print("Check")
```

> - [ ] False
> - [x] **True**
> - [ ] Check
> - [ ] 24 > 16 or 0

### Question 6

6. Fill in the blanks to complete the function. The “complementary_color” function receives a primary color name\
in all lower case, then prints its complementary color. Currently, the function only supports the primary colors\
of red, yellow, and blue. It returns "unknown" for all other colors or if the word has any uppercase characters.

```Python
def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement

print(complementary_color("blue")) # Should print orange
print(complementary_color("yellow")) # Should print purple
print(complementary_color("red")) # Should print green
print(complementary_color("black")) # Should print unknown
print(complementary_color("Blue")) # Should print unknown
print(complementary_color("")) # Should print unknown
```

### Question 7

7. Can you calculate the output of this code?

```Python
def difference(x, y):
    z = x - y
    return z

print(difference(5, 3))
```
*Output: 2*

### Question 8

8. What's the value of this Python expression?

```Python
x = 5*2

((10 != x) or (10 > x))
```

> - [ ] True
> - [x] **True**
> - [ ] 15
> - [ ] 10

### Question 9

9. Fill in the blanks to complete the “safe_division” function. The function accepts two numeric variables\
through the function parameters and divides the “numerator” by the “denominator”. The function’s main purpose\
is to prevent a ZeroDivisionError by checking if the “denominator” is 0. If it is 0, the function should return 0\
instead of attempting the division. Otherwise all other numbers will be part of the division equation.\
Complete the body of the function so that the function completes its purpose.

```Python
def safe_division(numerator, denominator):
    # Complete the if block to catch any "denominator" variables
    # that are equal to 0.
    if denominator == 0:
        result = 0
    else:
        # Complete the division equation.
        result = numerator /denominator
    return result

print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0
```

### Question 10

10. Code that is written so that it is readable and doesn’t conceal its intent is called what?

> - [ ] Intentional code
> - [ ] Maintainable code
> - [x] **Self-documenting code**
> - [ ] Obvious code