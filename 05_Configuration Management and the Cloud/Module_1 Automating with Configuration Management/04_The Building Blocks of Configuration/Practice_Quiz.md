# Practice Quiz:  The Building Blocks of Configuration Management

*Congratulations! You passed! Grade received 100%*

### Question 1

1. How is a declarative language different from a procedural language?

> - [x] **A declarative language defines the goal; a procedural language defines the steps to achieve a goal.**
> - [ ] Declarative languages are object-based; procedural languages aren’t.
> - [ ] Declarative languages aren’t stateless; procedural languages are stateless.
> - [ ] A declarative language defines each step required to reach the goal state. Correct

*In a declarative language, it's important to correctly define the end state we want to be in, without explicitly*\
*programming steps for how to achieve that state.*

### Question 2

2. Puppet facts are stored in hashes. If we wanted to use a conditional statement to perform a specific action based\
on a fact value, what symbol must precede the facts variable for the Puppet DSL to recognize it?

> - [ ] @
> - [ ] #
> - [x] **$**
> - [ ] &

*All variable names are preceded by a dollar sign in Puppet's DSL.*

### Question 3

3. What does it mean that Puppet is stateless?

> - [ ] Puppet retains information between uses.
> - [ ] An action can be performed repeatedly without changing the system after the first run.
> - [ ] **There is no state being kept between runs of the agent.**
> - [ ] Actions are taken only when they are necessary to achieve a goal.

*Stateless means there is no record of previous interactions, and each interaction request has to be handled based*\
*entirely on information that comes with it.*

### Question 4

4. What does the "test and repair" paradigm mean in practice?

> - [ ] There is no state being kept between runs of the agent.
> - [ ] We should plan to repeatedly fix issues.
> - [ ] We need to test before and after implementing a fix.
> - [x] **We should only take actions when testing determines they need to be done to reach the requested state**

*By checking to see if a resource requires modification first, we can avoid wasting precious time.*

### Question 5

5. Where, in Puppet syntax, are the attributes of a resource found?

> - [x] **Inside the curly braces after the resource type**
> - [ ] In brackets after the if statement
> - [ ] After ensure =>
> - [ ] After the dollar sign ($)

*We specify the package contents inside the curly braces, placed after the package title.*