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
# code from original sheet
import pandas as pd
df.loc[:, 'height'] = [1.7, 1.5, 1.6, 1.8]
df.loc[:, 'weight'] = [70, 51, 58, 90]


#### the answer ####
# first, define slices of the height and weight
# remember to use quotation marks.
h = df.loc[:, 'height']
w = df.loc[:, 'weight']

# do the BMI calculation. The exponent **2 takes
# precedence over the / divide operation so we
# don't need brackets.
bmi_for_all_rows = w / h ** 2

# alternatively, you can write it all on one line
# where you slice and do the math all together.
bmi_for_all_rows = df.loc[:, 'weight'] / df.loc[:, 'height'] ** 2

# checking the result
print(bmi_for_all_rows)

# set the value of a new column named 'bmi'.
# remember that the left-hand-side of an equals is
# what is being SET, and the right-hand-side is the value
# that you want to set it.
# So I want to SET df.loc[:, 'bmi'] to the value of bmi.
df.loc[:, 'bmi'] = bmi_for_all_rows


print(df)



# """
# **********************
# EXERCISE 2
# """
# Option 1
boolean_is_weight_below_threshold = df.loc[:, 'weight'] < 60
slice_below_weight = df.loc[boolean_is_weight_below_threshold, 'names']
print('weights less than 60 kg = \n', slice_below_weight)

# Option 2 - clearer because you define each item separately
w = df.loc[:, 'weight'] # the slice of weight values
rows_below_weight_threshold = (w < 60) # a True/False boolean array
slice_below_weight = df.loc[rows_below_weight_threshold, :]
names_of_slice_below_weight = slice_below_weight.loc[:, 'names']
print('weights less than 60 kg = \n', names_of_slice_below_weight)
#
# """
# **********************
# EXERCISE 3
# """
# #
import pandas as pd
df = pd.read_excel('data/oncotarget-edited.xlsx')

print('\n\n\ndf =\n', df.head(1))

print('columns are:')
print(df.columns)

# SLICES

log2_ratio = df.loc[:, 'log2(Parental/Resistant ratio)']
log10_pvalue = df.loc[:,'−log10(p-value)']

# BOOLEAN ARRAY of peptide count > 1
bool_array_peptide_count_more_than_one = df.loc[:, 'Peptide count'] > 1

# slicing out those rows with peptide count > 1
rows_with_peptide_count = df.loc[bool_array_peptide_count_more_than_one, :]

"""
CONCLUSION EXERCISE
"""
# # plot the slice
# import matplotlib.pyplot as plt
#
# rows_with_peptide_count.plot(x='log2(Parental/Resistant ratio)',
#                              y='−log10(p-value)',
#                              kind='scatter')
# plt.show()