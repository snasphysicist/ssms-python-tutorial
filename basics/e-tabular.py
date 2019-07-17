"""
TUTORIAL 5 - tabular data
"""

"""
The scientist often deals with data tables in text or excel.

Pandas is a great way to import and manipulate tabular data

You can install it from the TERMINAL using the command:

pip install pandas

Go ahead and try this.

The statement:
    
    import <insert_package_here> as <alias>
    
will import the specified package and allow you to name them as <alias>.
This is easier for typing than the long name.

"""

import pandas as pd
filepath = 'data/simpledata.xlsx'
df = pd.read_excel(filepath)
print('dataframe read in was:\n', df)

"""
A DataFrame is basically an Excel Spreadsheet in Python.
Notice how the columns and rows of the table are the same 
as what you would see in Ms Excel?

SLICING
When you want to get a value, specify the row and column
When you want to select a range, specify the rows and columns
You can do math operations on values, just like Excel

A slice is a constrained "view" of the dataframe.
You only view the cells you are interested in. 

The advantage? You can use layers of logic to select only
the rows or columns you want. 

E.g. 
more than 1 unique peptide,
> 3 multiple detections of the same analyte within 1 minute
interpolate to fill in missing data points
Calculate FDR q-values and filter those > 0.05  

"""




"""
SLICING 

To access data within dataframes, you must create a "slice".
A slice is defined by integers specifying rows and columns.

Use the .loc[row name, column name] or .iloc[row number, column number]

ALWAYS TWO PARAMETERS! ROWS and COLUMNS
If you use a name of a row/column you must use the quotation marks.
To tell the .loc and .iloc that you want to see all the items, use
a colon symbol :. The colon : means to apply no filter.
"""

# print('\na single value:', df.loc[1, 'names'])
# # Same thing but using .iloc and column numbers instead
# print('\nalternative way of getting single value:', df.iloc[1,0])
# #
# print('\na column slice:\n', df.loc[:,'age'])
# # Same thing but using .iloc and row numbers instead
# print('\nalternative way to slice a column\n',df.iloc[:,1])
# #

"""
If instead of a single row and column, you give the .loc function 
a list or an array, you will slice multiple rows/columns.

     .loc[  [row1, row5, rowX]  ,  [column4, column9, columnX] ]

"""

# print('\nmultiple columns:\n', df.loc[:,['names', 'age']])
# # Notice here the list [0,3] is being passed the the .loc
# # There are TWO pairs of square brackets with one for the .loc
# # and the other for the list

# .loc[ [multiple rows] ,  :  ]
# print('\nmultiple rows:\n', df.loc[[0,3],:])

"""
You can even add columns to the dataframe,
but the data you give it must have the same number of entries
"""

# # make a copy of the dataframe for us to play with
# df_copy = df.copy(deep=True)
# print('\nOriginal dataframe is:\n', df_copy)
#
# # create a new column called 'hair color'
# df_copy.loc[:,'hair color'] = ['black', 'red'] # WRONG
# df_copy.loc[:,'hair color'] = ['black', 'red', 'green', 'black'] # CORRECT
# df_copy.loc[:,'hair color'] = ['black', 'red', 'green', 'black'] # CORRECT
# print(df)
#
# # create a new now
# # WRONG because the df_copy now has a third column of 'hair color'
# df_copy.loc[4,:] = ['simon', 10]
# # CORRECT because we are giving the new row 3 values, which
# # exactly matches the existing dataframe.
# df_copy.loc[4,:] = ['simon', 10, 'blue']
#
# print('df with extra values:\n', df_copy)

"""
you can do math operations on slices
"""
# # Recall that you can multiply using the asterisk
# eg. 5*2 means five multiplied by two.

# print('\nmultiplying age by 2\n', df.loc[:,'age']*2)
#
# # Recall that adding two strings will join them together
# 'first string ' + 'next string' # an example.
# print('\nappending a string to the names\n', df.loc[:,'names'] + '_jones')


"""
EXERCISE 1
For this exercise I will add two columns of height and weight to the
DataFrame. Run this code here 
"""
# df.loc[:, 'height'] = [1.7, 1.5, 1.6, 1.8]
# df.loc[:, 'weight'] = [70, 51, 58, 90]
# print('\nmodified df =\n', df)

"""
EXERCISE 1 - continued
Note that slicing using the column/row names requires the quotation marks!
WRONG   -> df.loc[:, height]
CORRECT -> df.loc[:, 'height']

1. calculate the BMI for these four people given below. 
    BMI = weight(kg) / height(m)**2
2. add the BMI as a new column, called 'bmi'. I like keeping it lowercase 
    because it prevents typos.


YOUR CODE GOES HERE:
"""








"""
Advanced slicing

What if you want to slice the df based on the value?
How do you slice only those with height above 1.6 m?

This will combine what we know about Boolean and slices.
Applying a comparison operator == >= > < produces a True/False 
array. Each True/False corresponds to each item in the dataframe.
"""

# height = df.loc[:, 'height']
# #
# print('\nheights are \n', height)
# #
# those_above_threshold = (height > 1.6)

#
# print('\nthose above threshold =\n', those_above_threshold)

"""
We can use this boolean array to slice the dataframe.
True -> show
False -> hide

We will apply this boolean array to the rows (1st position),
because we want to display the rows of those who were above the height. 
"""

# details_above_threshold = df.loc[those_above_threshold, :]

# alternatively
# details_above_threshold = df.loc[[True,False,False,True], :]

# print('\ndetails of those above threshold\n', details_above_threshold)

"""
If you wanted just a subset of the details, you can slice the slice.
And you can keep slicing something until you get the info you want.

Here, I will slice the slice. I shall use two columns to show you. 
"""
# first_slice    = df.loc[those_above_threshold, :]
# slice_of_slice = df.loc[those_above_threshold, :].loc[:,'names']
# slice_of_slice2 = df.loc[those_above_threshold, :].loc[:,['names', 'age']]
# #
# print('\nslice of slice:\n', slice_of_slice)
# print('\nslice of slice2:\n', slice_of_slice2)


"""
EXERCISE 2

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

# # this opens the file you want to write to
# writer = pd.ExcelWriter('data/bmi_data.xlsx')
#
# # outputs the contents of df into the excel file you specified
# df.to_excel(writer)
#
# # save the excel file
# writer.save()

"""
Double click the file on the project navigator to the left and
check if the file is what you expected.
"""

"""
EXERCISE 3

We will examine a breast cancer dataset and look at a 
parental vs resistant cell line.

1. import pandas and load the data/oncotarget_pvals.xlsx file into a DataFrame    
2. check if the file loaded correctly by looking at the first row with
    the function print(df.head(1)). Does it match the excel file?
3. examine the columns using print(df.columns)
4. Make a series of slices:
    a. slice out the column 'log2(Parental/Resistant ratio)' and assign 
        to a variable
    b. slice out the column '−log10(p-value)' and assign to another variable
5. Make a boolean array of those rows with 'Peptide count' > 1 and assign
    to a variable
6. Use the boolean array to slice out the rows with peptides > 1  

YOUR CODE GOES HERE (I've started three lines for you)
"""

# import pandas as pd
# filepath = 'data/oncotarget_pvals.xlsx'
#
# # note the name of the dataframe is not "df"
# df_oncotarget = pd.read_excel('data/oncotarget-edited.xlsx')

"""
Reference:
SKBR3 proteomic reference:
Creedon, H., Gómez-Cuadrado, L., Tarnauskaitė, Ž., Balla, J., Canel, M., MacLeod, K. G.,
 … Brunton, V. G. (2016). Identification of novel pathways linking epithelial-to-mesenchymal 
 transition with resistance to HER2-targeted therapy. Oncotarget, 7(10), 11539–11552. 
 https://doi.org/10.18632/oncotarget.7317
"""

"""
CONCLUSION - Easy plotting

This is the final segment.

We will proceed to plot some of the data. You will see how easy it is
to plot data from a DataFrame!

You will need to install the matplotlib package in terminal:

>pip install matplotlib

Steps:
1. use DataFrame.plot(x= , y= , kind= )
2. then show the plot using plt.show()

x : label or position, default None
y : label, position or list of label, positions, default None
Allows plotting of one column versus another

kind : str
‘line’ : line plot (default)
‘bar’ : vertical bar plot
‘barh’ : horizontal bar plot
‘hist’ : histogram
‘box’ : boxplot
‘kde’ : Kernel Density Estimation plot
‘density’ : same as ‘kde’
‘area’ : area plot
‘pie’ : pie plot
‘scatter’ : scatter plot
‘hexbin’ : hexbin plot

"""
# this imports the "pyplot" subfolder in the matplotlib package.
# and we are using the alias "plt"
import matplotlib.pyplot as plt

# # re-specifiying the height and weight columns in case we've changed them.
# df.loc[:, 'height'] = [1.7, 1.5, 1.6, 1.8]
# df.loc[:, 'weight'] = [70, 51, 58, 90]
#
# # using the .plot function, you just specify which columns to use for x and y axes,
# # and the parameter "kind" can be used to specify what kind of plot you want.
# df.plot(y='age', x='names', kind='bar')
#
# # This show function is necessary to display the plot
# plt.show()
#
# df.plot(x='names', y='height', kind='barh')
# plt.show()

"""
EXERCISE 4

We can very easily plot a volcano plot!

Using the template above,

plot a "scatter" plot to have:
    x-axis column 'log2(Parental/Resistant ratio)',
    y-axis column '−log10(p-value)' 
    
Remember to use the correct dataframe!
"""