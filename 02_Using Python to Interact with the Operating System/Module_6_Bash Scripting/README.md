# Bash Scripting

In this module, you’ll be exposed to what the Linux OS has to offer and you'll learn about Bash scripting. We’ll go over\
basic Linux commands and explore the many processes Linux has to offer, including a key concept called redirection.\
We’ll then deep dive into creating bash scripts using variables and globs. Finally, we’ll learn about advanced bash\
concepts and develop an understanding of when to use bash versus Python.

## Learning Objectives

- Use basic Linux commands to work with files and directories
- Create bash scripts and execute them
- Execute scripts using variables and globs to influence the output of these scripts
- Utilize while and for loops in bash scripts
- Describe when it’s necessary to use Bash scripts over Python scripts

## Interacting with the Command Line Shell

### Basic Linux Commands

**Managing files and directories:**

```bash
$ cd directory_name  # changes the current working directory to the specified one
$ pwd  # prints the current working directory
$ ls  # lists the contents of the current directory
$ ls -l  # lists the additional information for the contents of the directory  
$ ls -a  # lists all files, including those hidden  
$ ls -la  # applies both the -l and the -a flags
$ mkdir directory_name  # creates the directory with the received name
$ rmdir directory_name  # deletes the directory with the received name (if empty)
$ cp old_name new_name  # copies old_name into new_name
$ mv old_name new_name  # moves old_name into new_name
$ touch file_name  # creates an empty file or updates the modified time if it exists
$ chmod modifiers files  # changes the permissions for the files according to the provided
# modifiers; we've seen +x to make the file executable
$ chown user files  # changes the owner of the files to the given user
$ chgrp group files  # changes the group of the files to the given group
```

**Operating with the content of files:**

```bash
$ cat file_name  # shows the content of the file through standard output
$ wc file_name  # counts the amount of characters, words, and lines in the given file;
# can also count the same values of whatever it receives via stdin
$ file file_name  # prints the type of the given file, as recognized by the operating system
$ head file_name  # shows the first 10 lines of the given fil
$ tail file_name  # shows the first 10 lines of the given fil
$ less file_name  # scrolls through the contents of the given file (press "q" to quit)
$ sort file_name  # sorts the lines of the file alphabetically)
$ cut -dseparator -ffields file_name  # for each line in the given file, splits the line 
# according to the given separator and prints the given fields (starting from 1)
```

**Additional commands:**

```bash
$ echo "message"  # prints the message to standard output
$ date  # prints the current date
$ who  # prints the list of users currently logged into the computer
$ man command # shows the manual page of the given command; manual pages contain a lot of
# information explaining how to use each command (press "q" to quit)
$ uptime  # shows how long the computer has been running
$ free  # shows the amount of unused memory on the current system
```

### Redirecting Streams

By default, the input is provided by the keyboard at the text terminal and the output and error are shown on the screen.\
This is the case not only for our Python scripts, but for all system commands.\
**Redirection** is a process of sending a stream to a different destination.

> *To redirect the standard output of a program to a file we use the ">" symbol.*\
> *If we want to append the redirected standard out to a file we can use the ">>" sign instead of ">"*

In a similar way we can also redirect **standard input**. Instead of using the keyboard to send data into a program,\
we can use the **"<"** symbol to read the contents of a file.

It can also be useful to redirect **STDERR** or to capture errors and diagnostic messages from a program.\
This can be done by using the character combination **2>** than similar to how we redirected **STDOUT** before.\

> *The number **2**, it represents the file descriptor of the **STDERR** stream.*\
*In this context you can think of a file descriptor as a kind of variable pointing to an IO resource.*\
*In this case the **STDERR** stream. **0** and **1** are the file descriptors for **STDIN** and **STDOUT**.*

**Managing streams:**

These are the **redirectors** that we can use to take control of the streams of our programs.

```bash
command > file  # redirects standard output, overwrites file
command >> file  # redirects standard output, appends to file
command < file  # redirects standard input from file
command 2> file  # redirects standard error to file
command1 | command2  # connects the output of command1 to the input of command2
```

### Pipes and Pipelines

There's another powerful way to perform **IO stream** redirection called **Piping**.\
Using pipes, you can connect multiple scripts, commands, or other programs together into a data processing pipeline.

> *Pipes connect the output of one program to the input of another!*

This means we can pass data between programs, taking the output of one and making it the input of the next.\
Pipes are represented by the **pipe** "|" character.

Example:

```bash
cat file.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
```

- *First using **cat** to get the contents of our file.txt file;*
- **tr** *takes the characters in the first parameter, in this case, it's a space and then transform them into a character*\
*in the second parameter. In this case, it's a newline character **(\n)**. So we're putting each word in its own separate line;*
- *Next, we pass results to the **sort** command through a pipe. This command sorts results alphabetically;*
- *The sorted results are then passed to the **uniq** command, which displays each match once, and by using a **-c** flag,*\
*it prefixes each unique line with a number of times it occurred;*
- *This output is passed via pipe to the **sort** command once more, this time, with the **-nr** flag, which sorts result*\
 *numerically and in reverse order;*
- *The output is finally passed to the **head** command, which prints the first 10 lines to STDOUT.*

### Signalling Processes

One way of communicating through the **pipelines** we learned about in the last video.\
Another way of communicating is through the use of **signals**.

 > ***Signals** are tokens delivered to running processes to indicate a desired action.*

Using signals, we can tell a program that we want it to pause or terminate. We can also cause it\
to reload its configuration, or to close all open files.

**Operating with processes:**

These are some commands that are useful to know in Linux when interacting with processes.

```bash
$ Ctrl-C  # sends a SIGINT signal to the program to stop processing cleanly
$ Ctrl-Z  # sends a SIGSTOP signal to the program to stop running without actually terminating
$ kill PID  # sends the SIGTERM signal to the process identified by PID
$ ps  # lists the processes executing in the current terminal for the current user
$ ps ax  # lists all processes currently executing for all users
$ ps e  # shows the environment for the processes listed
$ fg  # causes a job that was stopped or in the background to return to the foreground
$ bg  # causes a job that was stopped to go to the background
$ jobs  # lists the jobs currently running or stopped
$ top  # shows the processes currently using the most CPU time (press "q" to quit)
```

## Bash Scripting

### Using Variables and Globs

Bash lets us use variables to store and retrieve values. **Environment variables** that are set in the environment\
in which the command is executing. We mentioned that we set these variables using the **=** sign.\
When we want to access the value of a variable in bash, we need to prefix the name of the variable with the **$** sign.\
On top of the predefined environment variables, we can also define our own variables for our scripts.\
To do that we just assign a value to the name of the variable that we want to define.

Example:

```bash
$ example=hello
$ echo $example
$ # output: hello
```

> *Any variable that you define in your script or in the command line is **local** to the environment where you define it.*\
> *If you want commands from that environment to also see the variable you need to export them using the **export** keyword.*

**Globs** are characters that allow us to create list of files. The **\*** and **?** mark are the most common globs.

> *In bash, using a **\*** in the command line we'll match all filenames that follow the format that we specify!*\
> *Use a **\*** with no prefix or suffix which would match all the files in the current directory!*\
> ***?** symbol can be used to match exactly one character instead of any amount of characters!*

Example:

```bash
$ echo *.sh
$ # output: gather_info.sh gather_info_update.sh using_var_and_globs.sh
$ echo g*
$ # output: gather_info.sh gather_info_update.sh
$ echo *
$ # output: Bash Scripting Resources.docx gather_info.sh gather_info_update.sh Practice_Quiz.md using_var_and_globs.sh
$  echo ???????????.sh
$ # output: gather_info.sh
```

Using **globs** like this, lets us create list of files that we might operate on, like calling other commands\
in passing this list. If you want to use this functionality in Python, it's available through the **glob** module.

### Conditional Execution in Bash

In bash scripting, the condition used is based on the **exit status** of commands.\
We check the **exit status** for commands using the **$?**. And in bash scripting an **exit value** of **0** means success.

> *To create a **conditional expression**, we're going to call a command and if the exit status of that command is **0**,*\
*then the condition will be considered **true**.*
> *The **if** conditional ends with **fi** (a backwards "if").*

Bash script *"check_localhost.sh"*:

```bash
#!/bin/bash

ip="127.0.0.1"
path="/etc/hosts"

if grep $ip $path; then
    echo "Everything ok"
else
    echo "ERROR! $ip is not in $path"
fi
```

Run script:

```bash
$ ./check_localhost.sh
$ # output: 
127.0.0.1       localhost
127.0.0.1       kubernetes.docker.internal
Everything ok
```

There is plenty of other conditions that we might want to check in our scripts: if the file exists,\
if two strings are equal, if a number is less than another number, and so on.\
To help us with evaluating these conditions, there is a command called **Test**.

> ***Test** is a command that evaluates the conditions received and exits with **0** when they are true and with **1** when they're false.*

Example:

```bash
$ if test -n "$PATH"; then echo "Your path is not empty"; fi
$ # output: 
Your path is not empty
```

The **-n** option for the **test** command checks if a string variable is empty or not.

Another record of the previous example:

```bash
$ if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
$ # output: 
Your path is not empty
```

> ***[ ]** is an alias to the **test** command! there needs to be a **space** before the **closing bracket***

## Advanced Bash Concepts

### While Loops in Bash Scripts

**Loops** are what makes the computer do repetitive tasks for us, anything from working with a bunch of numbers\
to processing the contents of a file line by line.

While loop syntax:

```bash
while [ condition ]; do
    command 1
	command 2
	command 3
done
```

### For Loops in Bash Scripts

Both in Python and Bash, **for loops** are used to iterate over a sequence of elements.

> *In Python, the sequences are data structures like a list or a tuple or a string.*\
> *In Bash, we construct these sequences just by listing the elements with spaces in between.*

For loop syntax:

```bash
for VARIABLE in 1 2 3 4 5 .. N; do
    command 1
	command 2
	command N
done
```

or

```bash
for VARIABLE in file1 file2 file3; do
    command 1 on $VARIABLE
	command 2
	command N
done
```

or

```bash
for OUTPUT in $(Linux-Command-Here); do
    command 1 on $OUTPUT
	command 2 on $OUTPUT
	command N
done
```

### Choosing Between Bash and Python

Complex command:

```bash
for i in $(cat story.txt); d0 B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`; echo -n "${B}${i:1} "; done; echo -e "\n"
# output:
# Once Upon A Time There Was An Egg Of A Programming Language Called Python
```

When a **bash** command line starts becoming this complex, it's a better idea to write a **Python** script\
that handles data in a more readable and testable way. A simple script could look like this one:

> *capitalize_words.py*

```Python
#!/usr/bin/env python3

import sys

for line in sys.stdin:
	words = line.strip().split()
	print(" ".join([word.capitalize() for word in words]))
```

In this example, we take each line of standard input, remove the white space, and split it into separate words.\
Then, we use a list comprehension to capitalize each of the words and end up joining them back with spaces and\
printing the output. Once we have the script, we can execute it as part of a pipeline like this.

```bash
$ cat story.txt | ./capitalize_words.py
# output:
# Once Upon A Time There Was An Egg Of A Programming Language Called Python
```

> *So it's a good idea to choose **bash** when we're operating with **files** and **system commands**,*\
*as long as what we're doing is **simple** enough that the script is self-explanatory!*

> *As soon as it becomes **hard to understand** what the script is doing, it's better to write it in a more general scripting language like **Python**.*

Their availability depends on the platform that we're using. Some commands might not be present on certain operating systems.\
Running a **bash** script can get the job done very quickly on a **Linux** machine, but it won't work on a **Windows** machine.

If your code is **complex** or it needs to work **across platforms**, you might be better off using the **Python** standard library\
or other external modules that provide the same functionality.