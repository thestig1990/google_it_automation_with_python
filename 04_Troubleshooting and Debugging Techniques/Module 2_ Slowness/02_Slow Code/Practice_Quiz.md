# Practice Quiz:  Slow Code

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Which of the following is NOT considered an expensive operation?

> - [ ] Parsing a file
> - [ ] Downloading data over the network
> - [ ] Going through a list
> - [x] **Using a dictionary**

*Awesome! Using a dictionary is faster to look up elements than going through a list.*

### Question 2

2. Which of the following may be the most expensive to carry out in most automation tasks in a script?

> - [x] **Loops**
> - [ ] Lists
> - [ ] Vector
> - [ ] Hash

*Loops that run indefinitely, and include subtasks to complete before moving on can be very expensive for most automation tasks.*

### Question 3

3. Which of the following statements represents the most sound advice when writing scripts?

> - [ ] Aim for every speed advantage you can get in your code
> - [ ] Use expensive operations often
> - [x] **Start by writing clear code, then speed it up only if necessary**
> - [ ] Use loops as often as possible

*Awesome! If we don't notice any slowdown, then there's little point trying to speed it up.*

### Question 4

4. In Python, what is a data structure that stores multiple pieces of data, in order, which can be changed later?

> - [ ] A hash
> - [ ] Dictionaries
> - [x] **Lists**
> - [ ] Tuples

*Right on! Lists are efficient, and if we are either iterating through the entire list or*\
*are accessing elements by their position, lists are the way to go.*

### Question 5

5. What command, keyword, module, or tool can be used to measure the amount of time\
 it takes for an operation or program to execute? (Check all that apply)

> - [x] **time**
> - [x] **kcachegrind**
> - [x] **cProfile**
> - [ ] break

*Excellent! We can precede the name of our commands and scripts with the "time" shell builtin*\
*and the shell will output execution time statistics when they complete.*\
*Nice work! The kcachegrind tool is used for profile data visualization that, if we can insert*\
*some code into the program, can tell us how long execution of each function takes.*\
*Great job! cProfile provides deterministic profiling of Python programs, including*\
*how often and for how long various parts of the program executed.*