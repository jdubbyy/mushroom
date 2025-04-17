import numpy as np
import pandas as pd

#define a function to use in the for loop to calculate product of probability and log(probability)
def plogp(p):
    if p == 0:
        return 0
    else:
        return p*np.log2(p)

def Plot_Preparation(a, x, y):
    #x must be the attr_counts dataframe for the selected attr
    #y must be the attr_plogprob dataframe for the selected attr
    indep = x[a].sum(axis=1) / x[a].values.sum()
    dep = -1 * y[a].sum(axis=1)

    #resort by ascending entropy. apply resorted index to the independent proportion series
    sort_dep = dep.sort_values(ascending = True)
    sort_indep = indep.reindex(sort_dep.index)

    #commented out as i changed to a bar chart w variable widths
    #calculate cumulative series for independent proportion series
    #cum_sort_indep = sort_indep.cumsum()
    #sort_indep = cum_sort_indep - sort_indep

    #append the 100% value to finish the lines in the plot
    #sort_indep = pd.concat([sort_indep, pd.Series([1])])
    #sort_dep = pd.concat([sort_dep, pd.Series([1])])

    return [sort_indep, sort_dep, a]