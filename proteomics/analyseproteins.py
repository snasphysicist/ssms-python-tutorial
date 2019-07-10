# https://datascienceplus.com/proteomics-data-analysis-2-3-data-filtering-and-missing-value-imputation/
# https://datascienceplus.com/?s=proteomics+data+analysis
# https://www.ebi.ac.uk/pride/archive/projects/PXD002057

import pandas as pd
from scipy import stats
from statsmodels.stats import multitest

import statsmodels.api as sm
from statsmodels.formula.api import ols

import matplotlib.pyplot as plt

import numpy as np


f = 'data/proteinGroups for tutorial.txt'

df = pd.read_csv(f, sep='\t')

df_intensity = df.loc[:, [x for x in df.columns if 'Intensity' in x]]
df_intensity = np.log10(df_intensity)
# remove the -inf


# pvalue = df_intensity.apply(lambda x: stats.ttest_ind(x.values[1:4],x.values[4:7])[1], axis=1)

df['mean_intensity_parental'] = df_intensity.iloc[:, [1,2,3]].mean(axis=1)
df['mean_intensity_resistant'] = df_intensity.iloc[:, [4,5,6]].mean(axis=1)
df['ratio_resistant_over_parental'] = df.loc[:,'mean_intensity_resistant'] / df.loc[:,'mean_intensity_parental']

# df['pvalue'] = pvalue

data = df.iloc[:,[0] + list(range(48,54))]
data.columns=['id'] + ['parental']*3 + ['resist']*3

datastack = np.log(data.iloc[:15,:].set_index('id', drop=True))
# datastack = data.stack().reset_index().iloc[:15,:]
# datastack.columns = ['id', 'group', 'intensity']

print(datastack)

# plt.figure()
# plt.ion()
fig1, ax1 = plt.subplots(1,1)
ax1.set_title('Basic Plot')
a = ax1.boxplot(datastack)
plt.show()

# data['id'] = df['Protein IDs']

# p=plt
# datastack.iloc[:15,:].boxplot(column=0,by=['level_1'])
# plt.show()


#
#
# SSbetween = (sum(data.groupby('group').sum()['weight']**2)/n) \
#     - (data['weight'].sum()**2)/N



# reject_array, pvals_corrected, alpha_corrected_Sidak, alpha_corrected_Bonf = \
#     multitest.multipletests(pvalue, alpha=0.05, method='fdr_bh')
#
# hits_df = df.loc[reject_array,:]

# calculate the ratios

