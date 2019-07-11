"""

Start with the end in mind!
We want a volcano plot: x = fold change, y = p values .


functions needed:

take the pandas mean

do one way anova, explaining the two variable definition.
fstatistic, pvalue = stats.f_oneway(triplicates_parental.T, triplicates_resistant.T)
ie do two vars in the variables section.

visualisation exercise

save to excel

don't bother with pickle


"""

import pandas as pd
from scipy import stats
from statsmodels.stats import multitest
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_excel(f, skiprows=[0,1,2], header=None)
df = pd.read_excel('data/oncotarget_cut.xlsx',  header=[0,1])
# print(df)

# calculating the ratio of means
triplicates_parental = df.loc[:,'parental']
triplicates_resistant = df.loc[:,'resistant']
meanratio = triplicates_parental.mean(axis=1) / triplicates_resistant.mean(axis=1)
log_mean_ratio = np.log2(meanratio)

# calculating p-values using one way ANOVA
fstatistic, pvalue = stats.f_oneway(triplicates_parental.T, triplicates_resistant.T)

# FDR the reject_array is where you reject the hypothesis (that means are equal), ie. statistically different
reject_array, pvals_corrected, alpha_corrected_Sidak, alpha_corrected_Bonf = \
    multitest.multipletests(pvalue, alpha=0.01, method='fdr_bh')

# calculate the log P values
log_p_value = -np.log10(pvals_corrected)

# create a result table and populate it
result_df = pd.DataFrame()
result_df['uniprot'] = df.iloc[:,3]
result_df['name'] = df.iloc[:,4]
result_df['desc'] = df.iloc[:,5]
result_df['p_value_anova'] = pvalue
result_df['pvalue_fdr'] = pvals_corrected
result_df['logp'] = log_p_value
result_df['log2_mean_ratio'] = log_mean_ratio

# save to excel
writer = pd.ExcelWriter('output/result.xlsx')
result_df.to_excel(writer)
writer.save()

# plot volcano plot
p = plt
p.scatter(x=result_df['log2_mean_ratio'], y=result_df['logp'])
p.plot(result_df['log2_mean_ratio'],[-np.log10(0.05)]*len(result_df['log2_mean_ratio']), 'k-')

# label the top 3
top_5 = result_df.nlargest(n=3, columns='logp')
print(top_5)

for item in top_5.itertuples():
    print(item)
    p.text(s=item[2], x=item[7], y=item[6]+0.15, horizontalalignment='center')

p.show()



# print(result_df.iloc[result_df.loc[result_df['log2_mean_ratio']<-3, 'logp'].idxmax(),:].T)



