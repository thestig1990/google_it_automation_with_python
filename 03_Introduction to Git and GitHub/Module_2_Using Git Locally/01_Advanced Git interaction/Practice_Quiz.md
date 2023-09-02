# Practice Quiz: Advanced Git Interaction

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Which of the following commands is NOT an example of a method for comparing or reviewing the changes made to a file?

> - [ ] git log -p
> - [ ] git diff --staged
> - [ ] git add -p
> - [x] **git mv**

*Nice job! git mv won't give you any information on changes. Instead, it is used to move or rename a file or directory in Git.*

### Question 2

2. What is the gitignore file?

> - [ ] A file containing a list of commands that Git will ignore.
> - [ ] A file the user is intended to ignore.
> - [ ] A file listing uncommitted changes.
> - [x] **A file containing a list of files or filename patterns for Git to skip for the current repo.**

*Awesome! The gitignore file is a text file that tells Git which files or folders to ignore in a project.*

### Question 3

3. What kind of file will the command git commit -a not commit?.

> - [ ] Tracked files
> - [x] **New files**
> - [ ] Old files
> - [ ] Staged files

*Right on! Files that are new and untracked will not be committed before being added.*

### Question 4

4. What does HEAD represent in Git?

> - [ ] The subject line of a commit message
> - [ ] The top portion of a commit
> - [x] **The currently checked-out snapshot of your project**
> - [ ] The first commit of your project

*Awesome! We call the collection of edits we are making at one time a commit.*

### Question 5

5. If we want to show some stats about the changes in a commit, like which files were changed\
and how many lines were added or removed, what flag should we add to git log?

> - [x] **--stat**
> - [ ] --patch
> - [ ] -2
> - [ ] --pretty

*Excellent. This will cause git log to show some stats about the changes in the commit,*\
*like which files were changed and how many lines were added or removed.*