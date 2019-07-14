import pandas as pd
import numpy as np
# pprint.pprint allows nicer printing of values
from pprint import pprint

df = pd.read_excel('data/oncotarget_cut.xlsx', header=[0,1])
triplicates_parental = df.loc[:,'parental']
triplicates_resistant = df.loc[:,'resistant']

means_parental = triplicates_parental.mean(axis=1)
means_resistant = triplicates_resistant.mean(axis=1)
ratio_of_means = means_parental/means_resistant
log2_ratio_of_means = np.log2(ratio_of_means)

print('means of parental are:', means_parental.head(5))
print('means of resistant are:', means_resistant.head(5))
print('ratio of means are:', ratio_of_means.head(5))
print('log2 ratios are:', log2_ratio_of_means.head(5))

log10_pvalues = -np.log10()