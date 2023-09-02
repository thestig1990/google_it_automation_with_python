# Video Quiz: Code that Crashes

### Question 1

1. Which of the following can assist in finding out if invalid operations are occurring in a program running on a Windows system?

> - [ ] Valgrind
> - [x] **Dr. Memory**
> - [ ] PBD files  
> - [ ] Segfaults

*Dr. Memory can assist in finding out if invalid operations are occurring in a program running on Windows or Linux.*

### Question 2

2. What can you use to notify users when an error occurs, the reason why it occurred, and how to resolve it?

> - [ ] The pdb module
> - [x] **The logging module**
> - [ ] Use printf debugging
> - [ ] The echo command

*Excellent! The logging module sets debug messages to show up when the code fails.*

### Question 3

3. After getting acquainted with the program’s code, where might you start to fix a problem?

> - [ ] Run through tests
> - [ ] Read the comments
> - [x] **Locate the affected function**
> - [ ] Create new tests  

*Nicely done! Start working on the function that produced the error, and the function(s) that called it.*

### Question 4

4. YWhen debugging code, what command can you use to figure out how your program reached the failed state?

> - [ ] gdb
> - [x] **backtrace**
> - [ ] ulimit
> - [ ] list

*The backtrace command can be used to show a summary of the function calls that were used to the point where the failure occur.*

### Question 5

5. When debugging in Python, what command can you use to run the program until it crashes with an error?

> - [ ] pdb3
> - [ ] next
> - [x] **continue**
> - [ ] KeyError

*Running the continue command after starting the pdb3 debugger will execute the program until it finishes or crashes.*