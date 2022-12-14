# -*- coding: utf-8 -*-
"""assignment7.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LLmMGy8ui6Pp1hQwH64h2UvtU0_2JyDz
"""

#1. Is the Python Standard Library included with PyInputPlus?
---->

 PyInputPlus is not a part of the Python Standard Library, we must install it separately using Pip.

#2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
------>
  so that we can use shorter format for calling the function.

#3. How do you distinguish between inputInt() and inputFloat()?
---->
  
  inputInt(): accsept interger value where,
  inputFloat(): accsept float value .

#4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
------>

   By using :   pyip.inpuInt(min=1, max=100)

#5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
---->

  We can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes
  keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or
   reject as valid input.

#6. If a blank input is entered three times, what does inputStr(limit=3) do?
------>
   Ans. It will throw RetryLimitException exception.

#7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
------>
   When you use limit keyword arguments and also pass a default keyword argument, the function returns 
   the default value instead of raising an exception