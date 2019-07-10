"""
TUTORIAL 5 - tabular data
"""

"""
The scientist often deals with data tables in text or excel.

Pandas is a great way to import and manipulate tabular data

"""

import pandas as pd

filepath = 'data/simpledata.xlsx'

df = pd.read_excel(filepath)

print('dataframe read in was:\n', df)

"""
To access data within dataframes, you must create a "slice".
A slice is defined by integers specifying rows and columns.

Use the .loc[row name, column name] or .iloc[row number, column number]
"""

print('\na single value:', df.loc[1, 'names'])
print('\nalternative way of getting single value:', df.iloc[1,0])

print('\na column slice:\n', df.loc[:,'age'])
print('\nalternative way to slice a column\n',df.iloc[:,1])

print('\nmultiple columns:\n', df.loc[[0,1],['names', 'age']])

"""
You can even add columns to the dataframe,
but the data you give it must have the same number of entries
"""

# df.loc[:,'hair color'] = ['black', 'red']

# df.loc[4,:] = ['simon', 10]
#
# print('df with extra values:\n', df)

"""
you can do math operations on slices
"""
print('\nmultiplying age by 2\n', df.loc[:,'age']*2)

print('\nappending a string to the names\n', df.loc[:,'names'] + '_jones')

"""
EXERCISE

1. calculate the BMI for these four people. BMI = weight(kg / height(m)**2
2. add the BMI as a new column, called 'bmi'. I like keeping it lowercase 
because it prevents typos.
"""

df.loc[:, 'height'] = [1.7, 1.5, 1.6, 1.8]
df.loc[:, 'weight'] = [70, 51, 58, 90]

print(df)

"""
Advanced slicing

What if you want to slice the df based on the value?
How do you slice only those with height above 1.6 m?

This will combine what we know about Boolean and slices.
Applying a comparison operator == >= > < produces a True/False 
array. Each True/False corresponds to each item in the dataframe.
"""

height = df.loc[:, 'height']

print('\nheights are \n', height)

those_above_threshold = (height > 1.6)

print('\nthose above threshold =\n', those_above_threshold)

"""
We can use this boolean array to slice the dataframe.
True -> show
False -> hide

We will apply this boolean array to the rows (1st position),
because we want to display the rows of those who were above the height. 
"""

details_above_threshold = df.loc[those_above_threshold, :]

print('\ndetails of those above threshold\n', details_above_threshold)

"""
If you wanted just a subset of the details, you can slice the slice.
And you can keep slicing something until you get the info you want.

Here, I will slice the slice. I shall use two columns to show you. 
"""

slice_of_slice = df.loc[those_above_threshold, :].loc[:,'names']
slice_of_slice2 = df.loc[those_above_threshold, :].loc[:,['names', 'age']]

print('\nslice of slice:\n', slice_of_slice)
print('\nslice of slice2:\n', slice_of_slice2)


"""
EXERCISE

1. try to slice out of df those with weight below ("<") 60 kg
2. get the names of those who meet this criteria
3. print out the names
"""

"""
Saving your work

You can save dataframes as Excel files or comma separated values.
Do this by following the following structure.

Recall that pd is pandas
"""

# this opens the file you want to write to
writer = pd.ExcelWriter('data/bmi_data.xlsx')

# outputs the contents of df into the excel file you specified
df.to_excel(writer)

# save the excel file
writer.save()

"""
Double click the file on the project navigator to the left and
check if the file is what you expected.
"""