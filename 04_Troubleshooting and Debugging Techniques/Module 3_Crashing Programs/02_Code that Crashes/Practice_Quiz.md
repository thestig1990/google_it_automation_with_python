# Practice Quiz:  Code that Crashes

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Which of the following will let code run until a certain line of code is executed?

> - [x] **Breakpoints**
> - [ ] Watchpoints
> - [ ] Backtrace
> - [ ] Pointers

*Way to go! Breakpoints let code run until a certain line of code is executed.*

### Question 2

2. Which of the following is NOT likely to cause a segmentation fault?

> - [ ] Wild pointers
> - [ ] Reading past the end of an array
> - [ ] Stack overflow
> - [x] **RAM replacement**

*Right on! Segmentation fault is not commonly caused by a new RAM card in the system.*

### Question 3

3. A common error worth keeping in mind happens often when iterating through arrays or other collections,\
and is often fixed by changing the less than or equal sign in our for loop to be a strictly less than sign.\
What is this common error known as?

> - [ ] Segmentation fault
> - [ ] backtrace
> - [ ] The No such file or directory error
> - [ ] Off-by-one error

*Nice work! The Off-by-one bug, often abbreviated as OB1, frequently happens in computer programming*\
*when an iterative process iterates one time too many or too little.*

### Question 4

4. A very common method of debugging is to add print statements to our code that display information, such as contents\
of variables, custom error statements, or return values of functions. What is this type of debugging called?

> - [ ] Backtracking
> - [ ] Log review
> - [x] **Printf debugging**
> - [ ] Assertion debugging

*Excellent! Printf debugging originated in name with using the printf() command in C++ to display debug information,*\
*and the name stuck. This type of debugging is useful in all languages.*

### Question 5

5. When a process crashes, the operating system may generate a file containing information about the state\
 of the process in memory to help the developer debug the program later. What are these files called?

> - [ ] Log files
> - [x] **Core files**
> - [ ] Metadata file
> - [ ] Cache file

*Core files (or core dump files) record an image and status of a running process, and can be used to determine the cause of a crash.*