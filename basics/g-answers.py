"""
Answers to Stats
"""
"""
*******************
EXERCISE 1
"""

import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats import multitest

x = pd.DataFrame([[1,2,3], [6,7,8], [4,5,6], [7,8,9]], index=['protein'+x for x in '1234'], columns=['replicate'+x for x in '123'])
y = pd.DataFrame([[10,11,12], [5,6,7], [3,4,5], [1,2,3]], index=['protein'+x for x in '1234'], columns=['replicate'+x for x in '123'])

print('x=\n',x)
print('\ny=\n',y)

print('\n\ntransposed x=\n', x.T)
print('\ntransposed y=\n', y.T)

_, pvalue = f_oneway(x.T,y.T)

print('p-values for proteins are', pvalue)


"""
*****************
EXERCISE 2

1. Apply the one-way anova to the oncotarget intensities to obtain
    a list of p-values
"""


import pandas as pd
import numpy as np
# pprint.pprint allows nicer printing of values
from pprint import pprint

df = pd.read_excel('data/oncotarget_cut.xlsx', header=[0,1])
triplicates_parental = df.loc[:,'parental']
triplicates_resistant = df.loc[:,'resistant']

test_statistic, oncotarget_pvalues = f_oneway(triplicates_parental.T,
                              triplicates_resistant.T)

print('\n\noncotarget p values are:\n', oncotarget_pvalues[:5], '\n\n')

"""
************************
EXERCISE 3
"""

# do FDR
reject_boolean_array, pvals_corrected, _, _ = \
    multitest.multipletests(oncotarget_pvalues, alpha=0.05, method='fdr_bh')

# calculate the means and the log2 ratio of means
means_parental = triplicates_parental.mean(axis=1)
means_resistant = triplicates_resistant.mean(axis=1)
ratio_of_means = means_parental/means_resistant
log2_ratio_of_means = np.log2(ratio_of_means)

# check answers
print('means of parental are:\n', means_parental.head(5))
print('means of resistant are:\n', means_resistant.head(5))
print('ratio of means are:\n', ratio_of_means.head(5))
print('log2 ratios are:\n', log2_ratio_of_means.head(5))


df['fdr_p_values'] = pvals_corrected
df['log2ratios'] = log2_ratio_of_means

print(df.head(1).T)

writer = pd.ExcelWriter('data/oncotarget_pvals2.xlsx')
df.to_excel(writer)
writer.save()