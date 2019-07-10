"""
TUTORIAL 6 - functions
"""

"""
Functions are one of the hardest aspects of ALL coding.

Functions are a small operation with defined inputs and outputs.
Like a self-contained script.

You've already seen the sqrt function that takes in a number and 
returns the square root. Or the max function.

 Don't worry if you don't get this - functions take several attempts
 to understand. The work we will be doing can be done without functions,
 but functions often allow you to scale up your operations (from 1 to millions)

You always define "def" a function FIRST.
Then call/run it SECOND 

"""
# calling a function before it is defined will fail
# print('result =', increment_by_two(5))

# def increment_by_two(a):
#     print('\ninput was', a)
#     # the return statement ends the function and gives the value back to
#     # wherever it was called from.
#     return a + 2
#
# print('result =', increment_by_two(5))
#
# print('result =', increment_by_two(1001))

"""
You can see that instead of typing out this operation
for hundreds of values, you could just run this function
"""

# for x in [10,20,30,40,50,60]:
#     print('result =', increment_by_two(x))

"""
Functions can be used on dataframes too.

The .apply is used on dataframes to apply functions on the data.
The "axis" parameter is needed to tell it to go DOWN the list rather than ACROSS.
"""

# import pandas as pd
#
# def squarethis(a):
#     return a**2
#
# df = pd.DataFrame([1,2,3,4,5])
#
# print('the dataframe was:\n', df)
#
# result = df.apply(squarethis, axis=1)
# print('\nafter the function:\n', result)

"""
For simple math operations you don't need to use functions. 
But say you had 5 operations you wanted to do. You would 
have to create 5 different variables to store the intermediate 
result after each step.
"""
import pandas as pd

df = pd.DataFrame([[1.25, 1.5, 1.7, 1.63], [60,50,120,60]], index=['height','weight']).T

print('\nthe dataframe:\n', df, '\n')

bmi = df.loc[:,'weight'] / df.loc[:,'height']**2

print(bmi)

# alternatively, using functions

def bmi(height, weight):
    return weight / height**2

# x[0] and x[1] refer to the first and second values per row
# "lambda x" is a shortcut function where x is each row.
print('\nusing functions:\n', df.apply(lambda x: bmi(x[0],x[1]), axis=1))

"""
EXERCISE

1. write a function that will add together two values and square the result.
2. apply this function to the height and weight df
"""

def add_and_sqaure():
    ...

