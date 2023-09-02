# Testing in Python

In this module, you’ll learn how to create tests in Python. We’ll cover what testing is all about and dive into\
the differences between manual versus automated testing. Next, we’ll explore what unit tests are intended to do\
and how to write them. Then, we’ll learn about other test concepts like black box versus white box tests and how\
test-driven development can frame how you design and write your code. Finally, you’ll learn about errors and\
exceptions, and how to combat them.

## Learning Objectives

- Explain what testing is and the different types of testing available
- Describe the difference between black box and white box testing
- Explain test-driven development
- Apply a try-except construct to catch errors and exceptions

## Video materials for Module 5

[Link](https://drive.google.com/drive/folders/1cbJpn1J-09_xmB2F9mef2mtEdTbR0QB5?usp=sharing)

## Simple Tests

### What is testing?

> *Software testing is a process of evaluating computer code to determine whether or not it does what you expect it to do.*\
> *Software testing is similar in lots of ways to the tests performed in the manufacturing process of a new piece of machinery.*

Types of testing:

- Unit tests
- Integration tests
- System Tests

### Manual Testing and Automated Testing

- Manual testing:\
*Executing a script with different command-line arguments to see how its behavior changed is an example of manual testing.*

- Automated testing:\
*Formal software testing takes us process a step further, codifying tests into its own software and code that can be run to\
verify that our programs do what we expect them to do. This is called automatic testing. The goal of automatic testing is\
to automate the process of checking if the returned value matches the expectations.*

## Unit Tests

> *Unit tests are used to verify that small isolated parts of a program are correct.\
Unit tests are generally written alongside the code to test the behavior of individual pieces or units like functions or methods.\
Unit tests help assure the developer that each piece of code does what it's meant to do.*

**Our tests should never modify the production environment!**\
**An important characteristic of a unit test is Isolation!**

> *Python provides a module called unittest. This module includes a number of classes and methods that let us easily\
create unit tests for our code. The unittest module provides a test case class with a bunch of testing methods ready to use.*

**Edge cases:**
> *Edge cases are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of\
input we imagine our programs will typically work with. Edge cases usually need special handling in scripts in order for\
the code to continue to behave correctly.*

## Other Test Concepts

### Black box vs. White Box tests

- White Box tests:

> *White-box testing also sometimes called clear-box or transparent testing relies on the test creators knowledge of the software\
being tested to construct the test cases. With a white-box test, the test creator knows how the code works and can write test cases\
that use the understanding to make sure that everything is performing the way it's expected to*

- Black Box tests:

> *Written with an awareness of wahat the program is supposed to do - its requirements or specifications - but not how it does it*

### Other Test Types

- Unit test:

> *When we looked at unit tests, we call out they should focus on one specific unit, a functional method that being tested.\
This allows the test to verify the unit provides expected functionality regardless of the rest of the environment.*

- Integration test:

> *Integration tests verify that the interactions between the different pieces of code in integrated environments are working the way we\
 expect them to. While unit tests shouldn't cross boundaries to do things like make a network request or integrate with an API or database,\
the goal of an integration test is to verify these kinds of interactions and make sure the whole system works how you expect it to*

- Regression tests:

> *Usually written as part of a debugging and troubleshooting process to verify that an issue or error has been fixed once it's been identified.\
Say our script has a bug and we're trying to fix it. A good approach to doing this would be the first right to test fails by triggering the\
buggy behavior, then fix the bug so that a test passes. Regression tests are useful part of a test suite because they ensure that the same\
mistake doesn't happen twice.*

- Smoke tests:

> *Smoke test sometimes called build verification test, get their name from a concept that comes from testing hardware equipment.\
When writing software smoke test serve as a kind of sanity check to find major bugs in a program. Smoke test answer basic questions\
like, does the program run?*

- Load tests:

> *These tests verify that the system behaves well when it's under significant load. To actually perform these tests will need to generate\
traffic to our application simulating typical usage of the service. These tests can be super-helpful when deploying new versions of our\
applications to verify that performance does not degrade*

***Taking together a group of tests of one or many kinds is commonly referred to as a test suite. A good diversity of test types can\
create a more robust test suite that helps ensure your scripts and automation, do what you tell them to.***

### Test-Driven Development(TDD)

A process called test-driven development or TDD calls for creating the test before writing the code.\
The test-driven development cycle typically involves first writing a test then running it to make sure it fails.\
After all, you haven't written the code to make it passed yet. Once you've verified it fails, you write the code that\
will satisfy the test then run the tests again. If it passes you can continue on to the next part of your program. If it fails\
you Debug and run the test again. The cycle is repeated for each new feature of your script until it's up and running.

- Continuous Integration

> *When engineers submit their code, it's integrated into the main repository and tests are automatically run against it to spot bugs and\
errors in a process called Continuous Integration. Although useful, setting up a continuous integration process can be a big undertaking.*

## Errors and Exeptions

### The Try-Except Construct

When writing a try-except block, the important thing to remember is that the **code in the except block is only executed if one of the\
instructions in the try block raise an error of the matching type.** In this case, in the except-block, we're returning none to indicate\
to the calling code that the function wasn't able to do what was requested of it.

> *Returning "None" when something fails is a common pattern but not the only one. We could also decide to set a variable to some base\
value like zero for numbers, empty string for strings, empty list for list, and so on. It all depends on what our function does and\
what we need to get that work done.*

**The important point is that when we have an operation that might raise an error we want handle that failure gracefully by using the\
try-except block.** The operation could be opening a file, converting a value to a different format, executing a system command, sending\
data over the network or any other action that might fail and isn't trivial to check with a conditional.

> *An exception is not meant to produce an error, but to bypass it!*

### Raising Errors

- **raise**

The keyword to generate an error in Python is **raise**. We can raise a bunch of different errors that come already pre-built with Python\
or we can create our own, if the standard ones aren't good enough.

- **assert**

**assert** keyword tries to verify that a conditional expression is true, and if it's false it raises an assertion error with the indicated message.

> *Assert keyword is used to produce a message when a conditional is false.\
Assertions can be super helpful for debugging some code that's not behaving the way we expect it to.*

The **assert** statement exists in almost every programming language. It has two main uses:

> 1\. *It helps detect problems early in your program, where the cause is clear, rather than later when some other operation fails.\
A type error in Python, for example, can go through several layers of code before actually raising an Exception if not caught early on.\
> 2\. It works as documentation for other developers reading the code, who see the assert and can confidently say that its condition holds from now on.*

So as a rule, we should use **raise** to check for conditions that we expect to happen during normal execution of our code and **assert** to verify\
situations that aren't expected but that might cause our code to misbehave!

### Testing for Expected Errors

The **assertRaises** method provided by the unittest module  will raise an error while test that function.

**assertRaises()** – It allows an exception to be encapsulated, meaning that the test can throw an exception without exiting the execution, as is normally\
the case for unhandled exceptions. The test passes if exception is raised, gives an error if another exception is raised, or fails if no exception is raised.

There are two ways you can use assertRaises:

1. Using keyword arguments.

>> *assertRaises(exception, function, \*args, \*\*keywords)*

2. Using context manager.

>> *assertRaises(exception)*

Example:

```Python
import unittest

class MyTestCase(unittest.TestCase):

# Returns true if 1 + '1' raises a TypeError
def test_1(self):
	with self.assertRaises(Exception):
		1 + '1'

if __name__ == '__main__':
	unittest.main()
```