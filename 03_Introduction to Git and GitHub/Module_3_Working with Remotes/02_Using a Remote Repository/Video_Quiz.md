# Video Quiz: Using a Remote Repository

### Question 1

1. What will happen if the master repository receives a major update since the last local copy was synced?

> - [ ] Git will push your local copy.
> - [ ] Nothing will happen.
> - [x] **Git will let you know it's time for an update.**
> - [ ] Git will automatically merge the local copy with the master.

*Great job! If there are pending changes in the master branch, Git will let you know.*

### Question 2

2. If we want to make a change to a remote branch, what must we do?

> - [ ] Directly make the change
> - [ ] Use the git branch -r command
> - [x] **Pull the remote branch, merge it with the local branch, then push it back to its origin.**
> - [ ] Use the git remote -v command

*Excellent! We still have to go through the normal workflow to change remote branches.*

### Question 3

3. What’s the main difference between git fetch and git pull?

> - [x] **git fetch fetches remote updates but doesn't merge; git pull fetches remote updates and merges.**
> - [ ] git pull fetches remote updates but doesn't merge, while git fetch does.
> - [ ] git fetch clones the entire repository.
> - [ ] git pull requires a password while git fetch doesn't.

*Nice job! git pull instantly merges while git fetch only retrieves remote updates.*

### Question 4

4. Assuming no merge conflicts, which type of merge does git pull perform automatically?

> - [ ] Three-way merge
> - [ ] Explicit merge
> - [x] **Fast-forward merge**
> - [ ] Half-merge

*Awesome! As long as there are no conflicts, Git will move the current branch tip up to the target branch tip*\
*and combine histories of both commits.*