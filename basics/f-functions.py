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

NumPy was named from Numeric Python. It has almost all the math functions you'll ever need. 
https://www.datacamp.com/community/blog/python-numpy-cheat-sheet

"""

import numpy as np

x = [1,5,-2,8,6]

print('value of x =', x)

"""
See functions as little helpful tools

To find absolute value:
    Instead of having to say, if a number is negative, then invert it.
    Just use the in-built function np.abs(number)

"""

# print('absolute values of x =', np.abs(x))

"""
To find the sum:
    Instead of having to write a+b+c+d+...
    Just use np.sum(x)
    
And so on, for the different functions. Matrix math, geometry, etc.
"""

# print('sum of x is', np.sum(x))
# print('median of x is', np.median(x))
# print('25% quantile of x is', np.quantile(a=x, q=0.25))
# print('75% quantile of x is', np.quantile(a=x, q=0.75))
# print('sorted order of x is', np.sort(x))


"""
Some useful functions on dataframes.

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


"""
EXERCISE 1

We will do an exercise on the oncotarget dataframe again.
Copy your previous code to load the excel file into a dataframe.

For each dataframe, just display the top five rows using .head(5)
This conserves space while allowing you to check that the data is 
stored correctly.

1. on your slices of intensities, calculate the mean values for each row.
2. calculate the ratios of mean intensities for parental/resistant
3. calculate the logarithm base 2 of the means, using np.log2 <- Google numpy log2
4. print out your answers.

"""




"""
Custom Function

One of the HARDEST things to grasp about programming. Not absolutely
necessary for our final exercise, but this is useful for those who
want to progress further.

This is useful when you want to do multiple steps,
and you want to do it repeatedly. Instead of repeating
your code 100 times, you just "call" the function 100 times.

You always define "def" a function FIRST.
Then call/run it SECOND 

In many Python projects, all the functions come first in a file, 
and the main code that is executed comes at the end of a file.
"""

# # calling a function before it is defined will fail
# print('result =', bmi(1.62,55))

# def bmi(height, weight):
#     answer = weight / height**2
#     return answer
#
# print('result =', bmi(1.7, 55))
# print('result =', bmi(2.0, 120))


"""
EXERCISE 2 - Custom Functions

1. write a function named add_and_square that will add together two values and square the result.
2. apply this function to (45, 60)
"""

