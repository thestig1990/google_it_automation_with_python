# Practice Quiz: Undoing Things

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Let's say we've made a mistake in our latest commit to a public branch.\
 Which of the following commands is the best option for fixing our mistake?

> - [x] **git revert**
> - [ ] git commit --amend
> - [ ] git reset
> - [ ] git checkout -- <file>

*Nice job! git revert will create a new commit to reverse the previous one,*\
 *and is the best option for undoing commits on public branches.*

### Question 2

2. If we want to rollback a commit on a public branch that wasn't the most recent one\
 using the revert command, what must we do?

> - [ ] Use the git reset HEAD~2 command instead of revert
> - [ ] Use the revert command repeatedly until we've reached the one we want
> - [x] Use the commit ID at the end of the git revert command
> - [ ] Use the git commit --amend command instead

*Nice work! The commit ID is a 40-character hash that identifies each commit.*

### Question 3

3. What does Git use cryptographic hash keys for?

> - [ ] To secure project backups
> - [x] **To guarantee the consistency of our repository**
> - [ ] To encrypt passwords
> - [ ] To identify commits

*Woohoo! Git doesn't really use these hashes for security.*\
*Instead, they’re used to guarantee the consistency of our repository.*

### Question 4

4. What does the command git commit --amend do?

> - [ ] Start a new branch
> - [ ] Create a copy of the previous committ
> - [ ] Delete the previous commit
> - [x] **Overwrite the previous commit**

*The command git commit --amend will overwrite the previous commit with what is already in the staging area.*

### Question 5

5. How can we easily view the log message and diff output the last commit if we don't know the commit ID?

> - [x] **git show**
> - [ ] git identify
> - [ ] git log
> - [ ] git revert 

*Right on! The git show command without an object parameter specified*\
*will default to show us information about the commit pointed to by the HEAD.*