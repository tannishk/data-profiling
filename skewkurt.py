import scipy.stats as st
import pandas as pd

def skewness(dataset,col):
    "To Calculate the skewness of a given data For normal distribute data skewness = 0 , Skewness > 0 more weight the left tail and less weight in right tail "
    if(dataset[col].dtype == 'int64' or dataset[col].dtype == 'float64'):
        return st.skew(dataset[col])

def kurtosis(dataset,col,ty):
    "To calculate Kurtosis of a data set ty can be fisher or pearson"
    if (dataset[col].dtype == 'int64' or dataset[col].dtype == 'float64'):
        if(ty=='fisher'):
            fisherr = True
        else:
            fisherr = False
        return st.kurtosis(dataset[col], fisher=fisherr)

'''
data = pd.read_csv('bank.csv',';')
for i in data:
    print i

print skewness(data,'age')
print kurtosis(data,'day','fisher')
'''