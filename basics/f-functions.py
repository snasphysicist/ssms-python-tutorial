"""
TUTORIAL 6 - Functions

"""

"""
Functions are one of the HARDEST aspects of coding.
If you get this then you can learn almost any other language.

A Function is:
    a small 'operation' 
    with defined inputs 
    and an output

It is a self-contained list of commands that you can run whenever you want.

You've already seen the sqrt function that takes in a number and 
returns the square root. And the max function.

We will build custom functions just to understand them.

Don't worry if you don't get this - functions take several attempts
to understand. The work we will be doing can be done without custom functions,
but functions often allow you to scale up your operations (from 1 to millions)

"""

"""
Custom Functions

You always define "def" a function FIRST.
Then call/run it SECOND 

In many Python projects, all the functions come first in a file, 
and the main code that is executed comes at the end of a file.
"""

# calling a function before it is defined will fail
# print('result =', bmi(1.62,55))

def bmi(height, weight):
    answer = weight / height**2
    return answer

print('result =', bmi(1.7, 55))
print('result =', bmi(2.0, 120))


"""
EXERCISE

1. write a function named add_and_square that will add together two values and square the result.
2. apply this function to (45, 60)
"""

# def add_and_square(a, b):
#     # your code goes here
#
#
# print('result =', )

"""
Some useful functions on dataframes

(aren't you happy someone else coded these for you?)

len(object) --> get the length of object
 pd.DataFrame.mean() --> get the mean of the pandas DataFrame
"""

# x = [0,1,2,3,4]
# y = 'this is a string'
#
# print('length of x =', len(x))
# print('length of y =', len(y))
#
# print('\n\n')
#
# #-------------
#
#
# import pandas as pd
#
# df = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]])
#
# print('df =\n', df)
#
# print('mean of columns =\n', df.mean())
# print('mean of rows = \n', df.mean(axis=1))

