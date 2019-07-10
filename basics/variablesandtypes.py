"""
Tutorial 2 - variables and types
"""

"""
Variables are containers that you use to store data/values
The variable only comes into existence when you FIRST assign a value
You need to define the value of a variable before you ask the computer to use the variable

See how we correct the error below
"""

# my_first_variable = 1

my_first_variable + 5

print(my_first_variable)



"""
Python uses Types as efficient ways to store data.
Mismatches in Types are one of the most common errors.
Common Types:
1. Numbers - Integers and Floats
2. Strings 
3. Boolean - True or False
"""


"""
Numbers are either integers (int) or floating-point (float)
This is just how they are stored, because of the decimal place.
"""

# print('\nthis is an example of an integer')
# i = 5
# print('a =', i, type(i))
#
# print('\nthis is an example of a float')
# f = 5.0
# print('f = ', f, type(f))

"""
Python does math ok with a mix of integers and floats
"""

# print('\naddition = ', i + f)

"""
but often you cannot interchange int and float 
when feeding data into a program!

e.g. the round function takes in two arguments, 
1. the value to be rounded
2. the number of decimal places

Logic tells you that you cannot specify a fraction for the number of decimal places!
"""

# rounded_result = round(10.123456, 4)
#
# print('\nrounded result = ', rounded_result)
#
# rounded_result = round(10.123456, 4.5)
#
# print('\nsecond rounded result = ', rounded_result)

"""
How functions make sure that you don't feed them the wrong
TYPE of data is that they will check the data type.
If it is the wrong type, an error will be raised.

See example, even though I am putting in a "whole number",
if the function recognises it as a float, it will complain.
"""

# rounded_result = round(10.123456, float(4))
#
# print('\nthird rounded result = ', rounded_result)

"""
STRINGS
Used to store text
"""

s = 'this is a string'
s = "this is a string"
s = '''this is a string'''

# print('\n example of a string = ', s, type(s))

blank = ''

# print('\n example of a blank string = ', blank)

"""
You can "add" strings together
"""

joined_string = s + 'with another string joined'

# print('\n example of adding strings = ', joined_string, type(joined_string))

"""
Be careful with the spaces!
"""

"""
BOOLEAN

This data type makes it really efficient to compare different values. 
Either True or False

the double equals "==" is used to compare between two objects
the single equals "=" is used to set a value

"""

# boolean_variable = True
# boolean_variable = False

# print ('\nboolean variable: ', boolean_variable, type(boolean_variable))

# x = 1
# bool_comparison = x == 1

# print ('\nbool comparison to a correct value: ', bool_comparison, type(bool_comparison))

# bool_comparison = x == 'string'

# print ('\nbool comparison to a wrong value: ', bool_comparison, type(bool_comparison))

"""
EXERCISE

1. define a variable (name it what you want) and give it a value of 100.0
2. add 50 to the variable (hint: x = x + 1)
3. multiply by 2.5 (hint: use * )
4. divide by 3.1
5. print the variable out and check its type

6. define a second variable and give it a value of 'omics is awesome'
7. to this, add a string of ' and fun too!'
8. print out the variable to check you answer 

"""

# new_var =
# new_var = new_var +