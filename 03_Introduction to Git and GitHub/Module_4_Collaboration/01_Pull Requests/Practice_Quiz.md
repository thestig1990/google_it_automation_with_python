# Practice Quiz:  Pull Requests

*Congratulations! You passed! Grade received 100%*

### Question 1

1. What is the difference between using squash and fixup when rebasing?

> - [ ] Squash deletes previous commits.
> - [x] **Squash combines the commit messages into one. Fixup discards the new commit message.**
> - [ ] Squash only works on Apple operating systems.
> - [ ] Fixup combines the commit messages into one. Squash discards the commit message.

*Awesome! The fixup operation will keep the original message and discard the message from the fixup commit,*\
*while squash combines them.*

### Question 2

2. What is a pull request?

> - [ ] The owner of the target repository requesting you to add your changes.
> - [x] **A request sent to the owner and collaborators of the target repository to pull your recent changes.**
> - [ ] A request to delete previous changes.
> - [ ] A request for a specific feature in the next version.

*Right on! You send a pull request to the owner of the repository in order for them to incorporate it into their tree.*

### Question 3

3. Under what circumstances is a new fork created?

> - [x] **When you want to experiment with changes without affecting the main repository.**
> - [ ] When you clone a remote repository to your local machine.
> - [ ] During a merge conflict.
> - [ ] When there are too many branches.

*Nice work! For instance, when you want to propose changes to someone else's project,*\
*or base your own project off of theirs.*

### Question 4

4. What combination of command and flags will force Git to push the current snapshot to the repo as it is,\
 possibly resulting in permanent data loss?

> - [x] **git push -f**
> - [ ] git log --graph --oneline --all
> - [ ] git status
> - [ ] git rebase -i

*Awesome! git push with the -f flag forcibly replaces the old commits with the new one and forces Git to push*\
*the current snapshot to the repo as it is. This can be dangerous as it can lead to remote changes being permanently*\
*lost and is not recommended unless you're pushing fixes to your own fork (nobody else is using it)*\
*such as in the case after doing interactive rebasing to squash multiple commits into one as demonstrated.*

### Question 5

5. When using interactive rebase, which option is the default, and takes the commits and\
rebases them against the branch we selected?

> - [ ] squash
> - [ ] edit
> - [ ] reword
> - [x] **pick**

*Great job! The pick keyword takes the commits and rebases them against the branch we have chosen.*