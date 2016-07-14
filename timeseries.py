
# coding: utf-8

# In[44]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
from scipy.stats import stats
import statsmodels.tsa.api as sm
import statsmodels.stats.diagnostic as dm
import statsmodels.stats.stattools as k

from statsmodels.graphics import tsaplots
from statsmodels.tsa.seasonal import seasonal_decompose

##df = pd.read_csv('bank.csv',';')
def decompose(df,col,freq):
    "To plot the decomposition graphs "
    decomposed = seasonal_decompose(df[col].values, freq=freq)
    pd.DataFrame(decomposed.observed).plot(figsize=(12,4), title = "Observed")
    pd.DataFrame(decomposed.trend).plot(figsize=(12,4), title = "Trend")
    pd.DataFrame(decomposed.seasonal).plot(figsize=(12,4), title = "Seasonal")
    pd.DataFrame(decomposed.resid).plot(figsize=(12,4), title = "Residuals")
    
    
def freq(df,col,max1):
    "To find the required freq for the decompostion "

    count = None
    for i in range(1,max1):
        try:
            decomposed = seasonal_decompose(df[col].values, freq=i)
            decomposed.resid = decomposed.resid[[~np.isnan(decomposed.resid)]]
            print decomposed.resid
        ##decomposed.resid = [1,2,1,2,1,2]
            x = np.array(decomposed.resid)
            z,p = stats.kstest(x,'norm')
            if(p<0.055):
              print 'It is not the required freq'
            else:
                print 'it is the required freq'
                count = i
        except ValueError:
            pass
    decompose(df,col,i)
    return count
    
def lmtestcheck(df,col,max1):
    "To perform and LM test for autocorrelation and find significant lags . 1 to determine a significant lag and 0 to determine insignificant lag  "
    qstat, pval = sm.stattools.q_stat(sm.acf(df[col]), max1)
    j = []
    for i in pval:
        if(i<0.05):
            j.append(0)
        else:
            j.append(1)
    print pd.DataFrame({"Q statistic: ": qstat, "P value: ": pval})
    plt.scatter(qstat, pval)
    plt.hlines(0.05, min(qstat), max(qstat), colors = "r")
    plt.xlabel("Q statistic")
    plt.ylabel("p-value")
    plt.show()
    return j

def checkdb(df,col):
    "It also tells whether the Data is serially correlated or not "
    r = k.durbin_watson(df[col], axis=0)
    if(r==0):
        print "Not Serially correlated "
        return False,r
    else:
        print "Serially correlated "
        return True,r

    
def check(df,col):
    "To check whether a given series is Periodic or not using AutoCorrelation function :"
    x1acf = sm.acf(df[col])
    ##print x1acf
    plt.plot(x1acf)
    plt.xlabel("lags")
    plt.ylabel("ACF")
    plt.show()
    count=0
    for i in range(0,len(x1acf)):
        if((x1acf[i]<0.1 and x1acf[i]>0) or (x1acf[i]>-0.1 and x1acf[i]<0)):
            count=count+1
    print count        
    if(count>len(x1acf)/2):
        print "Data is random, 0 correlation "
    else:
        print "Data is periodic "


# In[45]:

#check(df,'balance')
##freq(df,'balance',365)


# In[ ]:



