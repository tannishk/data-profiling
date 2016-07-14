from sklearn.feature_selection import VarianceThreshold
import pandas as pd 
from sklearn.decomposition import PCA,FastICA
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
def varthres(dataset,threshold):
	"To do feature selction based on varience by passing the  threshold value  "
	sel = VarianceThreshold(threshold=threshold)
	X_new = sel.fit_transform(dataset)
	return X_new

def Kbest(df,features,class1,arr):
	"It is used to select arr number of best features based on chi test compared between features and  class1 which indicate the class to be predicted . Here df is the dataframe used  "
	X_new = SelectKBest(chi2, k=arr).fit_transform(df[features],df[class1])
	e = []
	##for i in X_new:
	##	e.append(i)
	g = list(X_new[0])
	count = 0
	for i in df.iloc[0].values:
		if(i in g):

			g.remove(i)
			e.append(features[count])
			count = count+1

	print e
	return X_new,e

def Pca(dataset,features,numberofcomponenets):
	"It is used to select the Principle component analysis for the given dataset with these features transforming it into data with number of componenets  "
	pca = PCA(n_components = numberofcomponenets)
	X_new = pca.fit_transform(dataset[features])
	print X_new
	return X_new

def Ica(dataset):
	"To do feature transformation such as all features are independent from one another "
	ica = FastICA()
	ds = ica.fit_transform(dataset)
	return ds
'''
df = pd.read_csv('iris.csv')
for i in df:
	print i 	
X_new,e = Kbest(df,['sepal_length','sepal_width','petal_length','petal_width'],'species',2)
X_new= Pca(df,['sepal_length','sepal_width','petal_length','petal_width'],2)
print X_new
'''