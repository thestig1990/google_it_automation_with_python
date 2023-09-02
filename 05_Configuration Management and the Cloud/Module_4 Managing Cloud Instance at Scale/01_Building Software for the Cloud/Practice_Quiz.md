# Practice Quiz:  Building Software for the Cloud

*Congratulations! You passed! Grade received 100%*

### Question 1

1. What is latency in terms of Cloud storage?

> - [ ] The measure of how many reads or writes you can do in one second, no matter how much data you're accessing.
> - [ ] The amount of data that you can read, and write in a given amount of time.
> - [x] **The amount of time it takes to complete a read or write operation.**
> - [ ] The time delay between an input and output.

*Latency is the amount of time it takes to complete a read or write operation.*

### Question 2

2. Which of the following statements about sticky sessions are true? (Select all that apply.)

> - [x] **All requests from the same client always go to the same backend server.**
> - [ ] Sticky sessions maintain an even load.
> - [x] **They should only be used when needed.**
> - [x] **They can cause problems during migration.**

*Sticky sessions route requests for a particular session to the same machine that first served the request for that session.*

*Because sticky sessions can cause uneven load distribution as well as migration problems, they should only be used when*\
*absolutely necessary.*

*Sticky sessions can cause unexpected results during migration, updating, or upgrading, so it's best to use them only*\
*when absolutely necessary.*

### Question 3

3. If you run into limitations such as rate limits or utilization limits, you should contact the Cloud provider and ask for a _____.

> - [ ] Beta version
> - [x] **Quota increase**
> - [ ] A/B test
> - [ ] Blob storage solution

*Our cloud provider can increase our limits that we have set, though it will cost more money.*

### Question 4

4. What is the term referring to everything needed to run a service?

> - [x] **Environment**
> - [ ] Provisions
> - [ ] Utilization limits
> - [ ] Continuous integration

*Everything used to run the service is referred to as the environment. This includes the machines and networks used for*\
*running the service, the deployed code, the configuration management, the application configurations, and the customer data.*

### Question 5

5. What is the term referring to a network of hosts spread in different geographical locations, allowing ISPs\
 to be as close as possible to content?

> - [ ] Domain Name Service
> - [ ] Continuous Deployment
> - [ ] Platform as a Service
> - [x] **Content delivery network**

*CDNs allow an ISP to select the closest server for the content it is requesting.*