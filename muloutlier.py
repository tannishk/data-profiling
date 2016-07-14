
# coding: utf-8

# In[56]:

import pandas as pd
from sklearn import svm
from sklearn import preprocessing
import matplotlib.pyplot as plt


def timeoutlier(dataset, col, window):
    "Outlier for time series throws a list with True is an outlier and false if not an outlier "
    x = pd.rolling_mean(dataset[col], window)
    y = pd.rolling_std(dataset[col], window)
    ##print x
    ##print y
    x1 = x.tolist()
    y1 = y.tolist()
    d1 = dataset[col].tolist()
    l = []
    for i in range(0,len(d1)):
        if(d1[i]>(x1[i]+(3*y1[i])) or d1[i] < (x1[i]-(3*y1[i]))):
            l.append(True)
        else:
            l.append(False)
       ## if(i>)
   ## plt.plot(dataset.index,dataset[col].tolist(),'ro', dataset.index,(x + (3 * y)),'b--', dataset.index,(x - (3 * y)),'g--')
    ##plt.show()
    return l

def transform(dataset,col):
    "Map all text data to numeric data returns an altered data frame "
    if(dataset[col].dtype=='object'):
        q = []
        r = []
        a = []
        for i in dataset.loc[:,col].unique():
            a.append(i)
        ##print a
        for i in dataset[col]:
            q.append(i)
        ##print q
        for i in q:
            r.append(a.index(i))
        ##print r
        dataset[col] = r
    return dataset

# In[ ]:





# In[57]:
def mulout(df):
    "Performs the preprocessing and uses oneclass SVM to find outliers in multi variate envirnment http://dl.acm.org/citation.cfm?id=1119749 "
    for i in df:
        if (df[i].dtype == 'object'):
            q = []
            r = []
            a = []
            for j in df.loc[:,i].unique():
                a.append(j)
            ##print a
            for j in df[i]:
                q.append(j)
           ## print q
            for j in q:
                r.append(a.index(j))
            ##print r
            df[i] = r

    ##print df
    df = preprocessing.scale(df)
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.03)
    clf.fit(df)
    y = clf.predict(df)
    print y
    count = 0
    outlier = 0
    for i in y:
        count = count + 1
        if (i == -1.0):
            print count, "is an outlier "
            outlier = outlier + 1
    print outlier
    return y
'''
df = pd.read_csv('ballon.csv',',')
print df
mulout(df)
'''
