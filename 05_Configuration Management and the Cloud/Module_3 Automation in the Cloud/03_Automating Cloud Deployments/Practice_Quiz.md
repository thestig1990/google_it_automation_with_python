# Practice Quiz:  Automating Cloud Deployments

*Congratulations! You passed! Grade received 100%*

### Question 1

1. In order to detect and correct errors before end users are affected, what technique(s) should we set up?

> - [x] **Monitoring and alerting**
> - [ ] Orchestration
> - [ ] Autoscaling
> - [ ] Infrastructure as Code

*Monitoring and alerting allows us to monitor and correct incidents or failures before they reach the end user.*

### Question 2

2. When accessing a website, your web browser retrieves the IP address of a specific node in order to load the site.\
 What is this node called?

> - [ ] Gate node
> - [x] **Entry point**
> - [ ] Access machine
> - [ ] Front line

*When you connect to a website via the Internet, the web browser first receives an IP address.*\
*This IP address identifies a particular computer: the entry point of the website.*

### Question 3

3. What simple load-balancing technique just assigns to each node one request at a time?

> - [ ] Random
> - [x] **Round Robin**
> - [ ] Least connections
> - [ ] Source IP

*Round-robin load balancing is a basic way of spreading client requests across a server group.*\
*In turn, a client request will be forwarded to each server.*\
*The load balancer is directed by the algorithm to go back to the top of the list and repeat again.*

### Question 4

4. Which cloud automation technique spins up more VMs into instance groups when demand increases,\
 and shuts down VMs when demand decreases?

> - [ ] Infrastructure as Code
> - [x] **Autoscaling**
> - [ ] Load Balancing
> - [ ] Orchestration

*Autoscaling helps us save costs by matching resources with demand automatically.*

### Question 5

5. Which of the following are examples of orchestration tools used to manage cloud resources as code? (Check all that apply)

> - [x] **Terraform**
> - [x] **CloudFormation**
> - [x] **Azure Resource Manager**
> - [ ] CloudFlare

*Like Puppet, Terraform uses its own domain specific language (DSL), and manages configuration resources as code.*

*CloudFormation is a service provided by Amazon to assist in modeling and managing AWS resources.*

*Azure Resource Manager is the deployment and management service for Azure. It provides a management layer that*\
*enables you to create, update, and delete resources.*