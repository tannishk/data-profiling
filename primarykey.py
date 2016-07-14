import pandas as pd
import numpy as np
def primarykey(dataset):
    "It is used to find a primary key in a given dataset "
    k = []
    for i in dataset:
        print i
        print len(dataset[i].unique()) ,  dataset[i].count()
        r = (len(dataset[i].unique()) / dataset[i].count())
        if(r > 0.85 ):
            k.append(i)

    return k

'''
data = pd.read_csv('ass',';')
print primarykey(data)
'''