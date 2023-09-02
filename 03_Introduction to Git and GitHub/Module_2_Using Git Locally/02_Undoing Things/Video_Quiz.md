# Video Quiz: Undoing Things

### Question 1

2. What is the purpose of the git checkout command?

> - [ ] It finalizes staged changes.
> - [x] **It reverts changes to modified files before they are staged**
> - [ ] It skips staging and directly commits..
> - [ ] It displays the current status of the commit.

*Right on! git checkout restores files to the latest stored snapshot, reverting any changes before staging.*

### Question 2

2. What does the git commit --amend do?

> - [ ] Add an error log to the commit.
> - [ ] Remove files from the staging area.
> - [ ] Change the commit message.
> - [x] **Overwrite the previous commit.**

*Awesome! git commit --amend allows us to modify and add changes to the most recent commit.*

### Question 3

3. Which of the following is true about the git revert command?

> - [ ] It undoes a commit as though it never happened.
> - [x] **It creates a new commit with inverse changes.**
> - [ ] The output of git revert is not the same as a regular commit.
> - [ ] It does not include the ID of the commit that was reverted.

*Awesome! With git revert, a new commit is created with inverse changes.*\
*This cancels previous changes instead of making it as though the original commit never happened.*

### Question 4

4. Which of the following is NOT true about the SHA1 hash numbers that Git uses to identify commits?

> - [ ] They provide the consistency that is critical for distributed systems such as Git.
> - [ ] They are created using the commit message, date, author, and the snapshot taken of the working tree.
> - [x] **Git requires the entire hash ID to identify a commit.**
> - [ ] They are composed of 40 characters.

*Git can identify a commit using the first few hash numbers as long as there is only one matching possibility.*
