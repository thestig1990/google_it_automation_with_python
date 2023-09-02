#!/usr/bin/env python3

import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)
  #--------debugg----------#
  # turn the number into a string using str() function.
  print("hello " + name + ", your random number is " + str(number))
  #--------debugg----------#

greeting()
