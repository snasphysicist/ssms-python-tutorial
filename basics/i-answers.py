"""
VISUALISATION ANSWERS
"""

"""
*****************
STATS EXERCISE 2

1. Apply the one-way anova to the oncotarget intensities to obtain
    a list of p-values
"""


import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats import multitest


df = pd.read_excel('data/oncotarget_cut.xlsx', header=[0,1])
triplicates_parental = df.loc[:,'parental']
triplicates_resistant = df.loc[:,'resistant']

test_statistic, oncotarget_pvalues = f_oneway(triplicates_parental.T,
                              triplicates_resistant.T)

print('\n\noncotarget p values are:\n', oncotarget_pvalues[:5], '\n\n')

"""
************************
STATS EXERCISE 3
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





"""
***************
VISUALISATION EXERCISE 1
"""

import numpy as np
import matplotlib.pyplot as plt

log10_pvalues = -np.log10(pvals_corrected)

p = plt
p.scatter(x=log2_ratio_of_means, y=log10_pvalues)
p.xlabel('log2(parental/resistant')
p.ylabel('-log10(p values)')

# to be fancy, you can plot a horizontal line making p=0.05
p.plot(log2_ratio_of_means.sort_values(),[-np.log10(0.05)]*len(log2_ratio_of_means), 'k--')

p.show()

