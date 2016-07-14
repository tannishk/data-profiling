
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse


r = "auto-mpg.csv"## Name of the file
d = "\s+"## delimiter

def is_date(string):
	"To check whether it is date datatype or not "
	try:
		return parse(string)
	except ValueError:
		return False
def uniqueoccur(dataset,name):
	"Frequency of each unique item in a dataset[name]"
	##list1 = dataset[name].unique()
	return dataset[name].value_counts()

def plot1(dataset,name):
	if(dataset[name].dtype=='int64' or dataset[name].dtype=='float64'):
		##dataset[name].plot.bar(stacked='true')
		dataset[name].plot.hist(alpha=0.5,color='red')
		##plt.axhline(0,color='')
		plt.show()

def rollingmean(dataset,name,win):
	"To calculate the rolling mean for a time series win :Size of the window "
	return pd.rolling_mean(dataset[name],win)

def rollingstd(dataset,name,win):
	"To calcualate the rolling Standard devaiation for a time sereis win:Size of the window "
	return pd.rolling_std(dataset[name],win)

def rangecol(dataset,name):
	"To give the range of the a column or the range of a given time stamp "
	max = dataset[name].max()
	min = dataset[name].min()
	print name , 'range from ',min,' to ',max

def type1(dataset,name):
	"TO give the data type a column whether it is float , integer , boolean ,String , Date datatype"
	type2 = dataset[name].dtype
	dataset[name].dropna()
	##print type2
	try:
		if(type2=='int64'):
			print name,'is of','Integer type'
		if(type2=='object'):
			a = dataset[name].unique()
			if(is_date(str(a[1]))):
				print name,'is of ','Date Type'
			elif( ('yes' in a and 'no' in a) or ('true' in a and 'false' in a) or ('t' in a and 'f' in a) or ('T' in a and 'F' in a)):
				print name,'is of ','boolean type'
			else:
				print name,'is of','String type'
		if(type2=='float64'):
			print name,'is of ','float type '
		return type2
	except Exception:
		print name,"is of ","String type "

		
def cal(dataset,name):
	"Used to display Sum , Average , mean , Median , Standard Deviation , Total Number of Values and Total Number of unique values "
	if(dataset[name].dtype == 'int64' or dataset[name].dtype == 'float64'):
		print 'Sum is ',dataset[name].sum()
		print 'Average is ' ,dataset[name].mean()
		print 'Median is ',dataset[name].median()
		print 'Standard deviation is ',dataset[name].std()
		print 'Total number of values in the column us ',dataset[name].count()
		print 'Number of unique values are',len(dataset[name].unique()) 
	else:
		print 'For this Columns No Numerical Features can be calculated '

def correlation(x,y):
	"Here x,y are 2 data series and used to find correlation between them . x,y should of float or Integer type and returns the pearson correlation cofficient and tell what type of correlation it is "
	if((x.dtype == 'int64' or x.dtype == 'float64') and (y.dtype == 'int64' or y.dtype == 'float64')):
		a = np.corrcoef(x,y)[0,1]
		if(a<0):
			print "Negative Correlation"
		elif(a>0):
			print "Positive Correlation"
		else:
			print "No Correlation"
		return a
	else:
		return False

def split(df,pos): ## function to split the dataset
	"Used to split the data between training and testing data and create test.csv and train.csv"
	count=1
	for row in df:
		count=count+1;## DO nothing
	print "Total rows are ",df[row].count()
	##pos = 400## Position where you want to split should be less then
	train = df[:pos]
	print train
	test = df[pos:df[row].count()]
	print test	
	train.to_csv('train.csv',index=True,header=True)
	test.to_csv('test.csv',index=True,header=True)

def desc(df,pos):
	"A similar to describe in describe with type and plot functionality "
	cal(df,pos)
	type1(df,pos)
	plot1(df,pos)
'''
df = pd.read_csv(r,d)
print df
a=[]
for i in df:
	a.append(i)
print "Total number of columns are ",len(a),"Columns are:" 
for i in a:
	print i 
	type1 = type(df,i)
	print type1
	print correlation(df[i],df['origin'])

col = 'origin'### Enter the Col name 
cal(df,col)
rangecol(df,col)
'''
