# Practice Quiz: Regular Expressions

*Congratulations! You passed! Grade received 100%*

### Question 1

1. When using regular expressions, which of the following expressions uses a reserved character\
 that can represent any single character?

> - [x] **re.findall(f.n, text)**
> - [ ] re.findall(f*n, text)
> - [ ] re.findall(^un, text)
> - [ ] re.findall(fu$, text)

*Nailed it! The dot (.) represents any single character.*

### Question 2

2. Which of the following is NOT a function of the Python regex module?

> - [ ] re.match()
> - [x] **re.grep()**
> - [ ] re.search()
> - [ ] re.findall()

*The grep command utilizes regular expressions on Linux, but is not a part of the standard re Python module.*

### Question 3

3. The circumflex [^] and the dollar sign [$] are anchor characters. What do these anchor characters do in regex?

> - [ ] Match the start and end of a word.
> - [x] **Match the start and end of a line**
> - [ ] Exclude everything between two anchor characters
> - [ ] Represent any number and any letter character, respectively

*Nailed it! the circumflex and the dollar sign specifically match the start and end of a line.*

### Question 4

4. When using regex, some characters represent particular types of characters. Some examples are the dollar sign,\
 the circumflex, and the dot wildcard. What are these characters collectively known as?

> - [x] **Special characters**
> - [ ] Anchor characters
> - [ ] Literal characters
> - [ ] Wildcard characters

*Special characters, sometimes called meta characters, give special meaning to the regular expression search syntax.*

### Question 5

5. What is grep?

> - [ ] An operating system
> - [ ] A command for parsing strings in Python
> - [ ] **A command-line regex tool**
> - [ ] A type of special character

*The grep command is used to scan files for a string of characters occurring that fits a specified sequence.*