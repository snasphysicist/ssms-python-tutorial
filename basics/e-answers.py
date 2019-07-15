"""
ANSWERS TO TABULAR
"""

"""
Getting the datafile used in the tutorial
"""
import pandas as pd
filepath = 'data/simpledata.xlsx'
df = pd.read_excel(filepath)
print('dataframe read in was:\n', df)

"""
**********************
EXERCISE 1
"""
import pandas as pd

df.loc[:, 'height'] = [1.7, 1.5, 1.6, 1.8]
df.loc[:, 'weight'] = [70, 51, 58, 90]

print(df)

"""
**********************
EXERCISE 2
"""

boolean_is_weight_below_threshold = df.loc[:, 'weight'] < 60
slice_below_weight = df.loc[boolean_is_weight_below_threshold, 'names']
print('weights less than 60 kg = \n', slice_below_weight)


"""
**********************
EXERCISE 3
"""
#
# import pandas as pd
# # pprint.pprint allows nicer printing of values
# from pprint import pprint
#
# df = pd.read_excel('data/oncotarget_cut.xlsx')
#
# print('\n\n\ndf =\n', df.head(5))
#
# print('columns are:')
# pprint(list(df.columns))
#
# # custom handling of the column headers.
# df = pd.read_excel('data/oncotarget_cut.xlsx', header=[0,1])
#
# print('columns are:')
# pprint(list(df.columns))
#
# print('triplicates of parental line are:\n', df.loc[:, 'parental'].head(5))
# print('triplicates of resistant line are:\n', df.loc[:, 'parental'].head(5))