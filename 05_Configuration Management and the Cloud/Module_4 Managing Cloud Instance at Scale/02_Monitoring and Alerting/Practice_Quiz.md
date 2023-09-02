# Practice Quiz:  Monitoring & Alerting

*Congratulations! You passed! Grade received 100%*

### Question 1

1. What is a Service Level Agreement?

> - [ ] An agreement between the user and developer.
> - [x] **A strict commitment between a provider and a client.**
> - [ ] An agreement between service providers.
> - [ ] A guarantee of service quality.

*A service-level agreement is an arrangement between two or more parties, one being the client and the other being service providers.*

### Question 2

2. What is the most important aspect of an alert?

> - [x] **It must be actionable.**
> - [ ] It must require a human to be notified.
> - [ ] It must require immediate action.
> - [ ] It must precisely describe the cause of the issue.

*If an alert notification is not actionable, it should not be an alert at all.*

### Question 3

3. Which part of an HTTP message from a web server is useful for tracking the overall status of the response\
 and can be monitored and logged?

> - [ ] A triggered alert
> - [ ] The data pushed back to the client
> - [ ] Metrics sent from the server
> - [x] **The response code in the server's message**

*We can log and monitor these response codes, and even use them to set alert conditions.*

### Question 4

4. To set up a new alert, we have to configure the _____ that triggers the alert.

> - [x] **Condition**
> - [ ] Metric
> - [ ] Incidents
> - [ ] Service Level Objective (SLO)

*We must define what occurence or metric threshold will serve as a conditional trigger for our alert.*

### Question 5

5. When we collect metrics from inside a system, this is known as ______ monitoring.

> - [x] **White-box**
> - [ ] Black-box
> - [ ] Network
> - [ ] Log

*A white-box monitoring system is one that collects metrics internally, from within the system being monitored.*