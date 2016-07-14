import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import stats
from mpl_toolkits.mplot3d import Axes3D
##from sklearn.decomposition import PCA
r = "bank.csv"## Name of the file
d = ";"## delimiter

def hisplot1(dataset,name):
	"It is used to create a histagram for a name column "
	dataset[name].hist(alpha=0.6)
	##plt.axhline(0,color='') 
	plt.show()

def lineplot(dataset,name):
	"Used to do autoscaling and plot line for group of data "
	dataset[name].plot()
	plt.show()

def threed(dataset,name):
	"Pass only 3 data columns to draw a 3d plot"
	threedee = plt.figure().gca(projection='3d')
	threedee.scatter(dataset[name[0]], dataset[name[1]], dataset[name[2]])
	threedee.set_xlabel(name[0])
	threedee.set_ylabel(name[1])
	threedee.set_zlabel(name[2])
	plt.show()

def outliers1(dataset,name):
	"IT is used to calculate univariate dataset based on Z test in a name column of the dataset"
	z= []
	for i in dataset[name]:
		z .append((i - dataset[name].mean()) / dataset[name].std(ddof=0))

	
	out = []
	for i in z:
		print i
		if(i > 3 or i < (-3)):
			out.append(1)
		else:
			out.append(0)
	return out		

def pca(dataset):
	count = 0
	for i in dataset:
		count = count+1
	pca = PCA(n_componenets=count)
	Z = pca.fit_transform(dataset)

def typedis(dataset,name,dis):
	"Type any type of ditribution . Dis is used to take in the type of code distribution visit refer http://docs.scipy.org/doc/scipy-0.14.0/reference/stats.html#module-scipy.stats for more reference and throws KS Test Statistic either D,D+,D-  test and p value as a result "
	if (dataset[name].dtype == 'int64' or dataset[name].dtype == 'float64'):
		dataset[name].dropna()
		x = np.array(dataset[name])
		z, p = stats.kstest(x, dis)
		if (p < 0.055):
			print 'It is Not as',dis,' distribution'
		else:
			print 'It is a',dis,'distribution'
		return z, p
	else:
		return None

def distri(dataset,name):
	"It is used to tell whether name of dataset is continous or a discrete distribution "
	if(dataset[name].dtype == 'object'):
		return 'discrete'
	else:
		len1 = len(dataset[name].unique()) /(dataset[name].count())
		if(len1 > 0.05):
			return 'continous'
		else:
			return 'discrete'

def norm(dataset,name):
	"Normal test for normal distribution and throws KS Test Statistic either D,D+,D-  test and p value as a result "
	if(dataset[name].dtype == 'int64' or dataset[name].dtype == 'float64'):
		dataset[name].dropna()
		x = np.array(dataset[name])
		z,p = stats.kstest(x,'norm')
		if(p<0.055):
			print 'It is Not a normal distribution'
		else:
			print 'It is a normal distribution'
		return z,p
	else:
		return None

def welisberg(dataset,name):
	"Weibull continous distribution and throws KS Test Statistic either D,D+,D-  test and p value as a result"
	if (dataset[name].dtype == 'int64' or dataset[name].dtype == 'float64'):
		dataset[name].dropna()
		x = np.array(dataset[name])
		z, p = stats.kstest(x, 'dweibull')
		if (p < 0.055):
			print 'It is Not a Weibull distribution'
		else:
			print 'It is a weibull distribution'
		return z, p
	else:
		return None


def exponential(dataset,name):
	"Exponential continous distribution and throws KS Test Statistic either D,D+,D-  test and p value as a result "
	if (dataset[name].dtype == 'int64' or dataset[name].dtype == 'float64'):
		dataset[name].dropna()
		x = np.array(dataset[name])
		z, p = stats.kstest(x, 'expon')
		if (p < 0.055):
			print 'It is Not a Exponential distribution'
		else:
			print 'It is a Exponential distribution'
		return z, p
	else:
		return None


def logistic(dataset,name):
	"Logistic continous distribution and and throws KS Test Statistic either D,D+,D-  test and p value as a result "
	if (dataset[name].dtype == 'int64' or dataset[name].dtype == 'float64'):
		dataset[name].dropna()
		x = np.array(dataset[name])
		z, p = stats.kstest(x, 'logistic')
		if (p < 0.055):
			print 'It is Not a Exponential distribution'
		else:
			print 'It is a Exponential distribution'
		return z, p
	else:
		return None



'''df = pd.read_csv(r,d)
print df	
for i in df:
	k = distri(df,i)
	z,p = norm(df,i)
	print i , ' is of ',k

a = outliers1(df,'age')
hisplot1(df,'weight')
##distribution(dar)'''