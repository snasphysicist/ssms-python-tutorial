"""
TUTORIAL 7 - Basic Statistics
"""
"""
Statistical analysis is often mysterious to us. The math is
often confusing. Thankfully, with Python, it doesn't have to be!

There are two Python packages that contain all the statistics
we need:

Scipy - scientific functions for python (incl. stats)
statsmodels - statistical functions for python

go ahead and install them (you can put all on the same line!):
pip install scipy statsmodels

Test if they work by importing them.
Watch out! with scipy, instead of import scipy you
will need to use a "from" statement.

This only imports one folder of scipy (which otherwise is HUGE)

"""

from scipy.stats import f_oneway
from statsmodels.stats import multitest

"""
The first test is the classic t-test. The t-test checks 
if there is a statistical difference between the means
of two groups of data.

e.g.
[A1,A2,A3] vs [B1,B2,B3]

Another name for the t-test is the one-way ANOVA 
(analysis of variance).
ANOVA is used when you have more than two groups of data,
but when you have only two groups, it is called "one-way"
and is actually the same as the t-test.

The method is: scipy.stats.f_oneway
We have already imported this as simply "f_oneway"

Googling this function:
https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.stats.f_oneway.html

Parameters:	
sample1, sample2, ... : array_like

The sample measurements for each group.

Returns:	
statistic : float

The computed F-value of the test.

pvalue : float

The associated p-value from the F-distribution.

-> so we need to feed f_oneway the different groups.

"""

# a = [4,5,6]
#
# b = [10,11,12]
#
# f_oneway_result = f_oneway(a,b)
#
# print('one way ANOVA result =', f_oneway_result)

"""
You should get:
F_onewayResult(statistic=54.0, pvalue=0.001826260668259983)

If p-value < 0.05 then we say that there is statistically 
significantly difference

This result actually has two parts, the test statistic (F)
and the pvalue.

You can use "unpacking" to split the result into two different
variables.
"""

# statistic, pvalue = f_oneway(a,b)
#
# print('one way ANOVA result =', statistic, 'and', pvalue)
# print('only the statistic =', statistic)
# print('only the p-value =', pvalue)

"""
IT'S DIFFICULT! ARE YOU STILL ALIVE??

EXERCISE 1

1. Apply the one-way ANOVA (t-test) to multiple groups

Note that f_oneway works on columns not rows, so we have to
"transpose" our data to appear in columns 
"""
# import pandas as pd
#
# x = pd.DataFrame([[1,2,3], [6,7,8], [4,5,6], [7,8,9]], index=['protein'+x for x in '1234'], columns=['replicate'+x for x in '123'])
# y = pd.DataFrame([[10,11,12], [5,6,7], [3,4,5], [1,2,3]], index=['protein'+x for x in '1234'], columns=['replicate'+x for x in '123'])
#
# print('x=\n',x)
# print('\ny=\n',y)
#
# print('\n\ntransposed x=\n', x.T)
# print('\ntransposed y=\n', y.T)
#
# _, pvalue = f_oneway(???)
#
# print('p-values for proteins are', pvalue)

"""
EXERCISE 2

1. Apply the one-way anova to the oncotarget intensities to obtain
    a list of p-values

"""


"""
Multiple Hypothesis Correction

If you run multiple t-tests over and over again hundreds of times,
statistically eventually you will end up with some false positives.

If you expect 5% errors, then 5 in 100 tests will appear significant!
That's 1 in 20. This is why we do replicates.

This happens A LOT when you have only 3 replicates and are doing the
t-test for 3000 proteins. You can't do 3000 triplicates. So we use 
something called correcting for multiple testing.

This is literally one-line in python (aren't you glad!).
"""

import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats import multitest

df = pd.read_excel('data/oncotarget_cut.xlsx', header=[0,1])
triplicates_parental = df.loc[:,'parental']
triplicates_resistant = df.loc[:,'resistant']

# as before, get the p values
_,pvalues = f_oneway(triplicates_parental.T, triplicates_resistant.T)

# how many hits were there?
boolean_array_of_hits = pvalues < 0.05
print('total proteins =', len(pvalues))
print('number of significant hits =', np.sum(boolean_array_of_hits))

# do FDR
reject_boolean_array, pvals_corrected, _, _ = \
    multitest.multipletests(pvalues, alpha=0.05, method='fdr_bh')

# reject array has True for below the alpha, and False for above the alpha
print('hits after FDR =', np.sum(reject_boolean_array))


print('example of before and after FDR =', round(pvalues[0],5), '<vs>', round(pvals_corrected[0],5),
      'which is',round(pvals_corrected[0]/pvalues[0],2),'times lower after FDR')

"""
Turns out that even with the FDR correction, most of the hits are still significant.

Now you know how to do the t-test and FDR correction!


EXERCISE 3

1. Add the code for multiple hypotheses correction and log2 meanratios to your answer
and check if they work.
2. create new columns containing these values in your dataframe. 
"""

"""

Take a break and review your notes.

Next, copy your dataset into the same folder as these scripts.

Use excel to make sure you've got the right columns: 
    protein/analyte intensities
    two conditions
    
"""


