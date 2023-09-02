# Practice Quiz: Managing Collaboration

*Congratulations! You passed! Grade received 100%*

### Question 1

1. How do we reference issues in our commits with automatic links?

> - [x] **By using one of the keywords followed by a hashtag and the issue number.**
> - [ ] By using an asterisk (*) after the issue number.
> - [ ] By typing the issue number inside braces ({}).
> - [ ] By using a special keyword.

*Right on! Keywords such as **closes** or **resolves** followed by a hashtag and the issue number will tell Git*\
*to autolink to the issue with the provided ID number.*

### Question 2

2. What is an artifact in terms of continuous integration/continuous delivery (CI/CD) pipelines?

> - [ ] An old and obsolete piece of code or library.
> - [x] **Any file generated as part of the CI/CD pipeline.**
> - [ ] An unintended minor glitch in a computer program
> - [ ] An automated series of tests that run each time there is a new commit or pull request.

*Awesome! Artifacts can include compiled code, test results, logs, or any type of file generated as part of the pipeline.*

### Question 3

3. Which of the following statements are good advice for project maintainers? (Check all that apply)

> - [ ] Coordinate solely via email
> - [x] **Reply promptly to pull-requests**
> - [x] **Understand any changes you accept**
> - [x] **Use an issue tracker**

*Woohoo! The more time that passes until a pull-request gets reviewed, the more likely it is that there's a new commit*\
*that causes a conflict when you try to merge in the change.*\
*Nice job! Not only do we not know whether the original coder is going to be around to maintain those functions,*\
*we also want to avoid feature creep and unmanageable code*
*Excellent! The larger our project grows, the more useful an issue tracker can be for collaborating.*

### Question 4

4. Which statement best represents what a Continuous Integration system will do?

> - [x] **Run tests automatically**
> - [ ] Update with incremental rollouts
> - [ ] Assign issues and track who's doing what
> - [ ] Specify the steps that need to run to get the result you want

*Nice job! A continuous integration system will build and test our code every time there's a change.*

### Question 5

5. Which statement best represents what a Continuous Delivery (CD) system will do?

> - [ ] Run tests automatically
> - [x] **Update with incremental rollouts**
> - [ ] Assign issues and track who's doing what
> - [ ] Specify the steps that need to run to get the result you want

*Right on! Continuous Delivery means new code is often deployed with the goal of*\
*avoiding rollouts with lots of changes between two versions.*