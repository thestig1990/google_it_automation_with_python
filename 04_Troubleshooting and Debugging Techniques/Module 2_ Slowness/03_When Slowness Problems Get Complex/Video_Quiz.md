# Video Quiz: When Slowness Problems Get Complex

### Question 1

1. A script is _____ if you are running operations in parallel using all available CPU time.

> - [ ] I/O bound
> - [ ] Threading
> - [x] **CPU bound**
> - [ ] Asyncio

*Right on! A script is CPU bound if you're running operations in parallel using all available CPU time.*

### Question 2

2. You’re creating a simple script that runs a query on a list of product names of a very small business,\
and initiates automated tasks based on those queries. Which of the following would you use to store product names?

> - [ ] SQLite
> - [ ] Microsoft SQL Server
> - [ ] Memcached
> - [x] **CSV file**

*Nice job! A simple CSV file is enough to store a list of product names.*

### Question 3

3. A company has a single web server hosting a website that also interacts with an external database server.\
The web server is processing requests very slowly. Checking the web server, you found the disk I/O has high latency.\
Where is the cause of the slow website requests most likely originating from?  

> - [x] **Local disk**
> - [ ] Remote database
> - [ ] Slow Internet
> - [ ] Database index

*You got it! The local disk I/O latency is causing the application to wait too long for data from disk.*

### Question 4

4. Which module makes it possible to run operations in a script in parallel that makes better use of CPU processing time? 

> - [ ] Executor
> - [ ] **Futures**
> - [ ] Varnish
> - [ ] Concurrency

*Woohoo! The futures module makes it possible to run operations in parallel using different executors.*