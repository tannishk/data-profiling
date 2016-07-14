#### 
import math 
import numpy as np
import scipy.spatial.distance as dist
from math import*  
### Euclids Distance
def euclids(x,y):
	"Euclids Distance "
	sum=0;
	for a,b in zip(x,y):
		sum = sum + math.pow(a-b,2)
	return math.sqrt(sum)
### Manhattan distance 
def manhattan(x,y):
	"Manhattan Distance "
	sum=0;
	for a,b in zip(x,y):
		sum=sum + abs(a-b)
	return sum
### Cosine Similarity 
def cosine(x,y):
	"Cosine Similarity "
	sum = 0
	for i in x:
		sum = sum+ (i*i)
	xs = math.sqrt(sum)
	sum = 0
	for i in y:
		sum = sum+ (i*i)
	ys = math.sqrt(sum)
	sum=0; 
	for a,b in zip(x,y):
		sum = sum + (a*b)
	xop = sum
	return xop / (xs*ys)




def MahalanobisDist(x, y):
	"MahalanobisDist"
	covariance_xy = np.cov(x, y, rowvar=0)
	inv_covariance_xy = np.linalg.inv(covariance_xy)
	xy_mean = np.mean(x), np.mean(y)
	x_diff = np.array([x_i - xy_mean[0] for x_i in x])
	y_diff = np.array([y_i - xy_mean[1] for y_i in y])
	diff_xy = np.transpose([x_diff, y_diff])

	md = []
	for i in range(len(diff_xy)):
		md.append(np.sqrt(np.dot(np.dot(np.transpose(diff_xy[i]), inv_covariance_xy), diff_xy[i])))
	return md


#def jaccard(x,y):
#	print 'hii'

def converttfidf(x,dictte):
	"To convert vector to tf  format "
	from collections import Counter 
	a=[]
	counts = Counter(x).values()
	for i in x:
		dictte[i] = dictte[i] + 1
	for j in dictte.values():
		a.append(j)
	return a


	



#from nltk.tokenize import word_tokenize
#k=[]
#example=['Mary had a little lamb' ,  'Jack went up the hill' , 'Jill followed suit' ,'i woke up suddenly','it was a really bad dream...']
#for i in example:
#	k.append(word_tokenize(i))
def createdict(a,b):
	"It is used to convert a , b to numeric vectors"
	c = a+b
	dict3 = {}
	dict1 = {}
	dict2 = {}
	for i in c:
		dict3[i] = 0
		dict1[i] = 0
		dict2[i] = 0
	##print dict3
	x=converttfidf(a,dict1)
	y=converttfidf(b,dict2)
	##print x
	##print y
	return x,y

def compare(a,b):
	"Find Cosine similarity between 2 columns of a and b dataframe  Code any be altered to include other similarity "
	for i in a:
		for j in b:
			if(a[i].dtypes==b[j].dtypes):
				x,y=createdict(a[i].tolist(),b[j].tolist())
				g = cosine(x,y)
				print '1st column is ',i,'2nd column is ',j ,' similarity is ', g
'''
import pandas as pd
a = pd.read_csv('bank.csv',delimiter=';')
b = pd.read_csv('iris.csv')
print a
print b
compare(a,b)
'''
