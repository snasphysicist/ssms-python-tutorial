"""
Tutorial 3 - LISTS
"""

"""
A list is a collection of objects.
Objects include such things as variables, numbers, strings, even functions!

Why put things into a list?
- can refer to things all at once, instead of one by one
- can iterate, ie. cycle through the list from start to finish
- you can extend the list without haivng to define new variables  
"""

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print('mylist =', mylist)

mylist2 = [1,2,3]

print('mylist2 =', mylist2)

"""
How you refer to specific positions in the list is
by giving it an integer corresponding to that position.

This integer must be enclosed in SQUARE BRACKETS. Not round brackets.

NOTE: in Python, virtually all list indexes start from zero!
i.e., 0, 1, 2, 3,...
Not 1, 2, 3,...
"""
#
# print(mylist[0]) # prints 1
# print(mylist[1]) # prints 2
# print(mylist[2]) # prints 3

"""
You can cycle through the list by using a for statement.

"FOR" x in VARIABLE
means that you are cycling through all the objects inside
VARIABLE one by one. Each time, you ask the code to refer
to the current object as "x".

"""

# # prints out 1,2,3
# for x in mylist:
#     print('for loop result = ', x)

"""
You can store variables in a list and "index" them
the same way.
"""

# x=10
# y=20
# z=20
#
# variable_list = [x,y,z]
#
# print('\nvariable list = ', variable_list)
#
# for x in variable_list:
#     print('variable list for loop result =', x)


"""
Common errors.

If you try to ask a list to give you a position that is
nonexistent, it will raise an error.

E.g. If you ask a list to give you its 10th value, but the 
list only has 3 values, it will fail.
"""

# mylist = [1,2,3]
#
# print('Attempting to get the 10th value...')
# print('tenth value is', mylist[9])

"""
EXERCISE

1. To a variable x, assign a blank list
2. Append to it your name and the name of those sitting to your left and right,
followed by their years in current position. ie name1, years1, name2, years2, ...  
3. Print out the first value from this list.
4. Try to print out the 100th variable from this list.
5. Try to get position "-1" from the list. What position is this?
6. Use a for loop to cycle through the list and print out each item
"""

# for current_name in list_of_friends_names:
#     print(...)