# Practice Quiz:  Introduction to GitHub

*Congratulations! You passed! Grade received 100%*

### Question 1

1. When we want to update our local repository to reflect changes made in the remote repository,\
 which command would we use?

> - [ ] git clone URL
> - [ ] git push
> - [x] **git pull**
> - [ ] git commit -a -m

*Right on! git pull updates the local repository by applying changes made in the remote repository.*

### Question 2

2. git config --global credential.helper cache allows us to configure the credential helper,\
 which is used for ...what?

> - [ ] Troubleshooting the login process
> - [ ] Dynamically suggesting commit messages
> - [ ] Allowing configuration of automatic repository pulling
> - [x] **Allowing automated login to GitHub**

*Nice work! By configuring the credential helper, we can avoid having to type in our username and\*
*password repeatedly.*

### Question 3

3. Name two ways to avoid having to enter our password when retrieving and when pushing changes to the repo.\
 (Check all that apply)

> - [ ] Implement a post-receive hook
> - [x] **Use a credential helper**
> - [x] **Create an SSH key-pair**
> - [ ] Use the git commit -a -m command.

*Awesome! The credential helper caches our credentials for a time window, so that we don't need to enter*\
 *our password with every interaction.*\
*Great job! We can create an SSH key-pair and store the public key in our profile, so that GitHub*\
 recognizes our computer.*

### Question 4

4. Name the command that gathers all the snapshots we've taken and sends them to the remote repository.

> - [ ] git commit -a -m
> - [x] **git push**
> - [ ] git pull
> - [ ] git clone URL

*Excellent! git push is used to update the remote repository with our local changes.*

### Question 5

5. 