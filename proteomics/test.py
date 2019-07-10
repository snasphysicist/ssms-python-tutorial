
import pandas as pd
from scipy import stats
from statsmodels.stats import multitest
import pickle

import statsmodels.api as sm
from statsmodels.formula.api import ols

import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_excel(f, skiprows=[0,1,2], header=None)
df = pd.read_excel('data/oncotarget.xlsx',  header=[0,1])

meanratio = df[['AZD8931-resistant SKBR3-AZDRc cells','Parental SKBR3 cells']].apply(lambda x: np.mean(x[3:]) / np.mean(x[:3]), axis=1)

pvalue = df[['AZD8931-resistant SKBR3-AZDRc cells','Parental SKBR3 cells']].apply(lambda x: stats.f_oneway(x[0:3],x[3:])[1], axis=1)

reject_array, pvals_corrected, alpha_corrected_Sidak, alpha_corrected_Bonf = \
    multitest.multipletests(pvalue, alpha=0.05, method='fdr_bh')
# the reject_array are where you reject the hypothesis (that means are equal), ie. statistically different

result_df = pd.DataFrame()
result_df['uniprot'] = df.iloc[:,3]
result_df['pvalue'] = pvals_corrected
result_df['logp'] = -np.log10(pvals_corrected)
result_df['log2_mean_ratio'] = np.log2(meanratio)

print(result_df.iloc[result_df.loc[result_df['log2_mean_ratio']<-3, 'logp'].idxmax(),:].T)

writer = pd.ExcelWriter('output/result.xlsx')
result_df.to_excel(writer)
writer.save()

with open('output/result.pkl', 'wb') as f:
    pickle.dump(result_df, f)

# plot volcano plot
p = plt
p.scatter(x=result_df['log2_mean_ratio'], y=result_df['logp'])
p.plot(result_df['log2_mean_ratio'],[-np.log10(0.05)]*len(result_df['log2_mean_ratio']), 'k-')
p.show()



