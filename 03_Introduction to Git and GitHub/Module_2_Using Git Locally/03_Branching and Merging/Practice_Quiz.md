# Practice Quiz: Branching and Merging

*Congratulations! You passed! Grade received 100%*

### Question 1

1. When we merge two branches, one of two algorithms is used. If the branches have diverged, which algorithm is used?

> - [x] **three-way merge**
> - [ ] git commit --amend
> - [ ] git reset
> - [ ] git checkout -- <file>

*Excellent! A three-way-mergeoccurs when the two commits have diverged previously, and a new commit is created.*

### Question 2

2. The following code snippet represents the result of a merge conflict.\
 Edit the code to fix the conflict and keep the version represented by the current branch.

```Python
<<<<<<< HEAD         
print("Keep me!")
=======
print("No, keep me instead!")
>>>>>>> brancho-cucamonga
```

Edited:

```Python
print("Keep me!")
```

*You got it! No more conflicts here!*

### Question 3

3. What command would we use to throw away a merge, and start over?

> - [ ] git checkout -b <branch>
> - [x] **git merge --abort**
> - [ ] git log --graph --oneline 
> - [ ] git branch -D <name>

*Right on! If there are merge conflicts, the --abort flag can be used to abort the merge action.*

### Question 4

4. How do we display a summarized view of the commit history for a repo, showing one line per commit?

> - [ ] git log --format=short 
> - [ ] git branch -D <name>
> - [x] **git log --graph --oneline**
> - [ ] git checkout -b <branch>

*Awesome! The commandgit log --graph --oneline shows a summarized view of the commit history for a repo.*

### Question 5

5. The following script contains the result of a merge conflict.\
 Edit the code to fix the conflict, so that both versions are included.

```Python
def main():
<<<<<<< HEAD
    print("Start of program>>>>>>>")
=======
    print("End of program!")
>>>>>>> improvement-to-the-code

main()
```

Edited:

```Python
def main():
    print("Start of program>>>>>>>")
    print("End of program!")
    
main()
```

*Great work! Now the code has both versions without anyconflicts!*