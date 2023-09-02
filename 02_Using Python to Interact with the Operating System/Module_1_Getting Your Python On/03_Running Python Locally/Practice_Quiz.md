# Practice Quiz: Running Python Locally

*Congratulations! You passed! Grade received 100%*

### Question 1

1. When your IDE automatically creates an indent for you, this is known as what?

> - [x] **Code completion**
> - [ ] Syntax highlighting
> - [ ] Interpreted language
> - [ ] Code reuse

*Nicely done! Code completion is an IDE feature that takes educated guesses about what you*\
*might be trying to type next, and offers suggestions to complete it for you.*

### Question 2

2. Can you identify the error in the following code?

```Python
#!/usr/bin/env python3
import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = numpy.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())
```

> - [ ] numpy is not imported correctly because as is used.
> - [x] **The y variable is not calling the numpy module properly.**
> - [ ] The shebang line is not necessary.
> - [ ] The function is not indented properly.

*Nice job! While the x variable is calling numpy using its declared local name,*\
*y is not using the local name. This will result in an error.*

### Question 3

3. Which type of programming language is read and converted to machine code before runtime, allowing for more efficient code?

> - [ ] Object-oriented language
> - [x] **Compiled language**
> - [ ] Interpreted language
> - [ ] Intermediate code

*A compiled language is translated into code readable by the target machine during development using a compiler.*

### Question 4

4. Which of the following is not an IDE or code editor?

> - [ ] Eclipse
> - [x] **pip**
> - [ ] Atom
> - [ ] PyCharm

*Right on! The package manager pip is used in Python to install packages from repositories such as PyPI.*

### Question 5

5. What does the PATH variable do?

> - [x] **Tells the operating system where to find executables**
> - [ ] Returns the current working directory
> - [ ] Holds the command line arguments of your Python program in a list
> - [ ] Tells the operating system where to cache frequently used files

*Nice work! The PATH variable tells the operating system where to find executables.*