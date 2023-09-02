# Practice Quiz: Python Subprocesses

*Congratulations! You passed! Grade received 100%*

### Question 1

1\. What type of object does a run function return?

> - [x] **CompletedProcess**
> - [ ] capture_output
> - [ ] stdout
> - [ ] returncode

*Awesome! This object includes information related to the execution of a command.*

### Question 2

2\. How can you change the current working directory where a command will be executed?

> - [ ] Use the shell parameter.
> - [ ] Use the env parameter.
> - [ ] Use the capture_output parameter.
> - [x] **Use the cwd parameter.**

*Right on! This will change the current working directory where the command will be executed.*

### Question 3

3\. When a child process is run using subprocess module, which o the following are true?

> - [x] **The child process is run in a secondary environment.**
> - [x] **The parent process is blocked while the child process finishes.**
> - [ ] The parent process and child process both run simultaneously.
> - [x] **Control is returned to the parent process when the child process ends.**

*Nice work! To run the external command, a secondary environment is created for the child subprocess, where the command is executed.*\
*Excellent! While the parent process is waiting on the subprocess to finish, it’s blocked, meaning the parent can’t do any work until the child finishes.*\
*Right on! After the external command completes its work, the child process exits, and the flow of control returns to the parent.*

### Question 4

4\. When using the *run* command of the subprocess module, what parameter, when set to True, allows us to store the output of a system command?

> - [ ] cwd
> - [x] **capture_output**
> - [ ] timeout
> - [ ] shell

*Excellent! The capture_output parameter allows us to get and store the output of the system command we're using.*

### Question 5

5\. What does the cope method of os.environ do?

> - [x] **Creates a new dictionary of environment variables**
> - [ ] Runs a second instance of an environment
> - [ ] Joins two strings
> - [ ] Removes a file from a directory.

*Nice work! The copy method of os.environ makes a new copy of the dictionary containing the environment variables, making modification easier.*