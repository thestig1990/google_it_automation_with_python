# Practice Quiz:  Handling Bigger Incidents

*Congratulations! You passed! Grade received 100%*

### Question 1

1. Which of the following would be effective in resolving a large issue if it happens again in the future?

> - [ ] Incident controller
> - [x] **Postmortem**
> - [ ] Rollbacks
> - [ ] Load balancers

*Keep it up! A postmortem is a detailed document of an issue which includes the root cause and remediation.*\
*It is effective on large, complex issues.*

### Question 2

2. During peak hours, users have reported issues connecting to a website. The website is hosted\
by two load balancing servers in the cloud and are connected to an external SQL database.\
Logs on both servers show an increase in CPU and RAM usage.\
What may be the most effective way to resolve this issue with a complex set of servers?

> - [ ] Use threading in the program
> - [ ] Cache data in memory
> - [x] **Automate deployment of additional servers**
> - [ ] Optimize the database

*You got it! Automatically deploying additional servers to handle the loads of requests during peak hours*\
*can resolve issues with a complex set of servers.*

### Question 3

3. It has become increasingly common to use cloud services and virtualization.\
 Which kind of fix, in particular, does virtual cloud deployment speed up and simplify?

> - [x] **Deployment of new servers**
> - [ ] Application code fixes
> - [ ] Log reviewing
> - [ ] Postmortems

*Right on! Virtualization makes deployment of VM servers in the cloud a fast and relatively simple process.*

### Question 4

4. What should we include in our postmortem? (Check all that apply)

> - [x] **Root cause of the issue**
> - [x] **How we diagnosed the problem**
> - [x] **How we fixed the problem**
> - [ ] Who caused the problem

*Sweet! In order to learn about the problem and how it happens in general, we should include what caused it this time.*\
*Awesome! By clarifying how we identified the problem, it can be more easily identified in the future.*\
*In order to share with reviewers how the issue was resolved, it's important to include what we did to solve it this time.*

### Question 5

5. In general, what is the goal of a postmortem? (Check all that apply)

> - [ ] To identify who is at fault
> - [x] **To allow prevention in the future**
> - [x] **To allow speedy remediation of similar issues in the future**
> - [ ] To analyze all system bugs

*Way to go! By describing the cause of the problem, we can learn to avoid the same circumstances in the future.*\
*By describing in detail how we fixed the problem, we can help others or ourselves fix the same problem more quickly in the future.*
