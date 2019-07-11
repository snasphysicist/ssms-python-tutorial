"""
TUTORIAL 1 - basics

use CTRL+` to get menu
use CTRL+/ to uncomment the block
"""

"""
to display something in the output console, use print()
"""

print("This line will be printed.")

"""
Variables, and setting the value of a variable

Left hand side is the variable you want to create (or change)
Right hand side is the value you want to assign to that variable
"""

# correct form
# x = 1

# wrong form
# 1 = x


"""
here, x is the variable you want to create.
1 is the value you want to assign to the variable x

you can check the value of x by printing it.
"""

# print(x)
# print('the value of x is', x)

"""
you can change the value stored in a variable
"""
# print('\nchanging value example:')
# x = 2
# print('the value of x is now', x)


"""
you can assign a variable to ANOTHER variable
"""

# z = x
# print('the value of z is ', z)

"""
leading spaces and indentations are IMPORTANT for python.
the convention is 4 spaces, or in Pycharm, a tab.
Don't use < 4 spaces, even though a single space works.

For example, this print statement will fail because it is indented for no reason:
"""

# x = 1
#     print('indented print statement worked')

"""
Indentation is used to mark a subsection such as a condition, or a loop.
The beginning of a subsection is marked with a colon ":"
"""
x=1
if x == 1:
    # indented 4 spaces, or a tab in pycharm
    print('\nindenting test:')
    print('x was found to be equal to 1')

"""
EXERCISE

1. Try assigning the value of 10 to a variable called y
2. Print out y to check
3. Try changing the value to 5 and printing to check.
"""

