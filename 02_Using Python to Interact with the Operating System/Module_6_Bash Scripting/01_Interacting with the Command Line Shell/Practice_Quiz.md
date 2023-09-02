# Practice Quiz: Interacting with the Command Line

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Which of the following commands will redirect errors in a script to a file?

> - [ ] user@ubuntu:~$ ./calculator.py >> error_file.txt
> - [ ] user@ubuntu:~$ ./calculator.py > error_file.txt
> - [ ] user@ubuntu:~$ ./calculator.py < error_file.txt
> - [x] **user@ubuntu:~$ ./calculator.py 2> error_file.txt**

*You nailed it! The "2>" sign will redirect errors to a file.*

### Question 2

2. When running a kill command in a terminal, what type of signal is being sent to the process?

> - [x] **SIGTERM**
> - [ ] SIGINT
> - [ ] PID
> - [ ] SIGSTOP

*You got it! The kill command sends a SIGTERM signal to a processor ID (PID) to terminate.*

### Question 3

3. What is required in order to read from standart input using Python?

> - [ ] echo file.txt
> - [ ] cat file.txt
> - [ ] The file descriptor of the STDIN stream
> - [x] **Stdin file object from sys module**

*Right on! Using sys.stdin, we can read from standard input in Python.*

### Question 4

4. ... are tokens delivered to running process to indicate a desired action?

> - [x] **Signals**
> - [ ] Methods
> - [ ] Functions
> - [ ] Commands

*Nice job! Using signals, we can tell a program that we want it to pause or terminate, or many other possible commands.*

### Question 5

5. In Linux, what command is used to display the contents of a directory?

> - [ ] rmdir
> - [ ] cp
> - [ ] pwd
> - [ ] **ls**

*Nice job! The ls command lists the file contents of a directory.*