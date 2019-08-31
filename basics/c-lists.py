"""
Tutorial 3 - LISTS
"""

"""
A list [] is a collection of objects.
Objects include such things as variables, numbers, strings, even functions!

Why put things into a list?
- can refer to things all at once, instead of one by one
- can iterate, ie. cycle through the list from start to finish
- you can extend the list without haivng to define new variables  

the append function takes only one item at a time.
"""

mylist = []
mylist.append(1)
mylist.append('two')
mylist.append(True)
mylist.append(6.4)
#
print('mylist =', mylist)
#
mylist2 = [1, 'two', True, 6.4]

print('mylist2 =', mylist2)

"""
How you refer to specific positions in the list is
by giving it an integer corresponding to that position.

This integer must be enclosed in SQUARE BRACKETS. Not round brackets.

NOTE: in Python, virtually all list indexes start from zero!
i.e., 0, 1, 2, 3,...
Not 1, 2, 3,...

List size has a maximum (of 5 million). If large number of 
items, use a numpy array.
"""

print(mylist[0])   # prints 1
print(mylist[1])   # prints 2
print(mylist[2])   # prints 3

"""
FOR LOOPS

How you might instruct someone to measure the
weights of every apple in a bag of apples?

One way is to tell them to pull one apple out of the bag
at a time, and weigh that apple, and then pick the next
apple.

This is the same idea when you want to go through items
in a list or a container.

You can cycle through a list by using a "for loop".

Syntax:
for <item> in <container>:
    do_action
    ...
    
Example using a Bag of Apples:
for current_apple in bag_of_apples:
    get_weight(current_apple)

You are cycling through all the objects inside
<container> one by one. Each time, you ask the 
code to refer to the current object as <item>.

You can name <item> as whatever you wish.

e.g. this achieves the same as the above.
for x in bag_of_apples:
    get_weight(x)

In the above example, x and current_apple are interchangeable.

Examples of for loops:
"""
mylist = []
mylist.append(1)
mylist.append('two')
mylist.append(True)
mylist.append(6.4)
#
print('\n\nmylist used in for loop =', mylist)
#
# # this is the counter we will use to keep track of the loops
iteration_counter = 0
#
# prints out values of mylist
for item in mylist:
    iteration_counter += 1
    print('\nthis is iteration', iteration_counter)
    print('the current item =', item)

# joins together all the values of mylist
answer = ''
#
# here, str(x) converts x into a string
# (cannot join string to different Types!)

for item in mylist:
    answer = answer + str(item)

print('\n\nThe combined string is', answer)

"""
Storing Variables in Lists 

You have seen us store numbers and strings in a list.

You can store variables in a list and "index" them
the same way. Indexing is the technical term for getting
a specific item out of a container/list.
"""

x = 10
y = 20
z = 30

variable_list = [x, y, z]
#
print('\nvariable list = ', variable_list)
#
for current_item in variable_list:
    print('variable list for loop result =', current_item)


"""
Common errors.

If you try to ask a list to give you a position that is
nonexistent, it will raise an error.

E.g. If you ask a list to give you its 10th value, but the 
list only has 3 values, it will fail.
"""

mylist3 = [1, 2, 3]
#
# print('Attempting to get the 10th value...')
# print('tenth value is', mylist3[10])

"""
first, run this file to make sure there aren't any errors before we start.

EXERCISE

1. To a variable x, assign a blank list
2. Append to it your name and the name of those sitting to your left and right,
    followed by their years in current position. 
    i.e. [name1, years1, name2, years2, ...]      
3. Print out the first value from this list.
4. Try to print out the 100th variable from this list (item 1 is at index 0).
5. Try to get position "-1" from the list. What position is this?
6. Use a for loop to cycle through the list and print out each item
"""

x = []

# for current_name in list_of_friends_names:
#     print(...)

