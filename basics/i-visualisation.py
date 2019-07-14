"""
TUTORIAL I - Visualisation
"""

"""
A key way for us to understand our data and to communicate it is
visualisation. Turning numbers into pictures helps us understand.

Making a plot and displaying the plot
Adding Scatter Plots
Exercise

"""


"""
Making a plot:

The most basic plotting package is matplotlib.
There is a special way to import matplotlib that you have to follow.

1. Create a plot and store it as a variable.
2. format the plot
3. add lines onto the plot
"""
import matplotlib.pyplot as plt

"""
you give the plot the x's and the y's separately.
matplotlib.pyplot.scatter(x, y, s=None, c=None, ...)
"""
p = plt
p.xlabel('x axis')
p.ylabel('y axis')
p.scatter(x=[0,1], y=[0,1], c='black')
# p.scatter(x=[1,3], y=[0,1], c='red')
# p.plot([2,4,6],[0,3,2], '--b')
p.show()
# p.close # will close the plot, if you need to

"""
Until you ask the plot to be shown, the plot will just accumulate
all the lines or scatters that you add onto it.
"""

"""
The challenge is often:
How do I get my data into x's and y's for plotting? 
"""

import pandas as pd
import matplotlib.pyplot as plt

# first load your data into a dataframe
df = pd.read_excel('data/bmi_data.xlsx')
print(df)

# then isolate the x and y values
xs = df['age']
ys = df['height']

p=plt
p.title('height vs age')
p.xlabel('age')
p.ylabel('height')
p.scatter(xs,ys, c='blue')
p.show()


"""
EXERCISE

We are going to do a volcano plot of the oncotarget proteins.

What is a Volcano Plot?
x-axis: log2 mean
y-axis: negative log10 of p-values

You previously calculated the log2 ratios of means on the oncotarget dataset.
You also calculated the p-values. But you'll need to turn these into 
-log10(p-value) 

1. proceed to add a new column containing the -log10(p-values)
2. create a plot and add a scatter using the log2 mean and -log10(p-values)
3. show the plot
4. Go back and label the axes correctly and give it a title. 
 
"""