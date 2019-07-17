"""
TUTORIAL 4 - importing packages
"""

"""
Intelligent people have created open source packages that you can use.

We want to use a spreadsheet package called "pandas".
To enable saving as Excel files, we will use the package "xlrd"

Go to "Terminal" (bottom of screen) and type in "pip install " followed by your 
package of interest and hit enter.

>pip install pandas 
>pip install xlrd 

alternatively, this will do the job too:
>pip install pandas xlrd

once completed, you can import the pandas package using an "import statement"
e.g.
import pandas

But pandas is a long name and it would make it much easier to use an abbreviation.

The "as" statement creates an alias for the package to a name you choose.
This is useful especially if you have long package names which are prone to typos.

import pandas as pd 

This statement means that you can access pandas using the abbreviation "pd".

Pandas has an in-built Type called DataFrame. 
This is Excel on steriods, as we will see.
"""

import pandas as pd

# you can then use data structures or functions that others have made
df = pd.DataFrame()

# checking the value
print('value of df =', df)

"""
you can also do the same with the popular mathematical package "numpy"

>pip install numpy

test one of the functions in numpy, e.g. sqrt for square root.

to pass a variable INTO a function, use brackets (not square brackets).

numpy lets you apply functions over arrays/lists, which is convenient
instead of doing it for each item individually.
"""

import numpy as np
print('testing square root =', np.sqrt(10))
print('testing square root for lists =', np.sqrt([1,2,3,4,5]))
#
# # trying to square root a list without numpy
# print('square root of [1,2,3,4,5] without numpy =', [1,2,3,4,5]**0.5)

"""
How do you get information on how to use packages?

Google them! For many packages, there is excellent documentation.
Google "pandas" or "numpy" to find more. Watch YouTube videos.
Search stackoverflow (website), or even post your own questions there!

"""

"""
EXERCISE

1. import numpy as np       <- see how Python reads like English?
2. use the np.max() function to find the maximum from "mylist".
3. try googling numpy mean 
"""
import numpy as np
mylist = [10,4,3,7,15,10]



"""
Important notes:

Always put all your import statements at the start of your code.
This makes it easier for someone else to know the packages your 
code requires BEFORE you begin.

Packages may have "dependencies", which are other packages that
they require you to install. 
"""

