# Practice Quiz:  Using a Remote Repository

*Congratulations! You passed! Grade received 100%*

### Question 1

1. In order to get the contents of a remote branch without automatically merging,\
 which of these commands should we use?

> - [ ] git pull
> - [x] **git remote update**
> - [ ] git checkout
> - [ ] git log -p -1

*You got it! git remote update will fetch the contents of all remote branches and allow us*\
*to merge the contents ourselves.*

### Question 2

2. If we need to find more information about a remote branch, which command will help us?

> - [ ] git fetch
> - [ ] git checkout
> - [ ] git remote update
> - [x] **git remote show origin**

*Right on! If you want to see more information about a particular remote branch,*\
 *you can use the git remote show command. Don't forget the commit ID!*

### Question 3

3. What command will download remote branches from remote repositories\
 without merging the content with your current workspace automatically?

> - [ ] git checkout
> - [ ] git pull
> - [x] **git fetch**
> - [ ] git remote update

*Nice work! git fetch will download remote updates, such as objects and refs, from the remote branch.*

### Question 4

4. What type of merge creates a new merge commit?

> - [ ] Fast-forward merge
> - [ ] Implicit merge
> - [x] **Explicit merge**
> - [ ] Squash on merge

*Woohoo! An explicit merge creates a new merge commit.*\
*This alters the commit history and explicitly shows where a merge was executed.*

### Question 5

5. What method of getting remote contents will automatically merge the remote branch with the current local branch?

> - [ ] git fetch
> - [ ] git checkout
> - [ ] git remote update
> - [x] **git pull**

*Great job! git pull automatically merges the remote branch with the current branch.*