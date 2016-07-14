dataset -- the Pandas data frame
colname -- The Column name 
In Split.py :
correlation(x,y):
	Here x,y are 2 data series and used to find correlation between them . x,y should of float or Integer type and returns the pearson correlation cofficient and tell what type of correlation it is

uniqueoccur(dataset,name):
	"Frequency of each unique item in a dataset[name]"

is_date(string):
	"To check whether it is date datatype or not "

rollingmean(dataset,name,win):
	To calculate the rolling mean for a time series , win:Size of the window

rollingstd(dataset,name,win):
	To calcualate the rolling Standard devaiation for a time sereis , win:Size of the window

RangeCol(dataset,colname)
To give the range of the a column or the range of a given time stamp 

type1(dataset,name):
	"TO give the data type a column whether it is float , integer , boolean ,String , Date datatype"

Cal(dataset,colname)
Used to display Sum , Average , mean , Median , Standard Deviation , Total Number of Values and Total Number of unique values 

Split(dataset,colname)
Used to split the data between training and testing data and create test.csv and train.csv

desc(df,pos):
	A similar to describe in describe with type and plot functionality

In replace.py :

rep(dataframe,col,choice,value):
	Tells about all the rows with which has an empty value for a particular column with an option to add / alter the values indicating empty values eg . NULL , NaN ,  , unknown etc and also allows a person to replace a given value" choice is used to tell your choice whether to replace the value or not , value to enter a value you want to replace it with

In featureselection.py
Kbest(dataset,features,class1,arr): It is used to select arr number of best features based on chi test compared between features and  class1 which indicate the class to be predicted . Here df is the dataframe used
PCA(dataset,numberofcomponenets) :It is used to select the Principle component analysis for the given dataset with these features transforming it into data with number of componenets
varthres(dataset,threshold):
	"To do feature selction based on varience by passing the  threshold value  "
Ica(dataset):
	"To do feature transformation such as all features are independent from one another "


In Distribution.py : 
distri(dataset,name): It is used to tell whether name of dataset is continous or a discrete distribution 
outlier(dataset,name): IT is used to calculate univariate dataset based on Z test in a name column of the dataset 
hisplot1(dataset,name): IT is used to create a histagram for a name column
lineplot(dataset,name):
	"Used to do autoscaling and plot line for group of data passed as a set of columns in a list "
threed(dataset,name):
	"Pass only 3 data columns as a list in name  to draw a 3d plot"
norm(dataset,name) : Normal test for normal distribution and throws normal test and p value as a result
welisberg(dataset,name):
	"Weibull continous distribution and throws KS Test Statistic either D,D+,D-  test and p value as a result"
exponential(dataset,name):
	"Exponential continous distribution and throws KS Test Statistic either D,D+,D-  test and p value as a result "
logistic(dataset,name):
	"Logistic continous distribution and and throws KS Test Statistic either D,D+,D-  test and p value as a result "
typedis(dataset,name,dis):
	"Type any type of ditribution . Dis is used to take in the type of code distribution visit refer http://docs.scipy.org/doc/scipy-0.14.0/reference/stats.html#module-scipy.stats for more reference and throws KS Test Statistic either D,D+,D-  test and p value as a result "

In Muloutlier.py:
transform(dataset,col):
Map all text dataset[col] in  to numeric data and returns an altered dataframe
mulout(df):
Performs the preprocessing and uses oneclass SVM to find outliers in multi variate envirnment 
timeoutlier(dataset, col, window):
Outlier for time series throws a list with True is an outlier and false if not an outlier

In similarity.py:

createdict(a,b): 
It is used to convert a , b to numeric vectors 

Euclids(x,y):
to find euclid similarity 
Manhattan (x,y):
To find manhattan similarity 
Cos(x,y):
to find cosine similarity
MahalanobisDist(x, y):
to find MahalanobisDist

converttfidf(x,dicte):
To convert a x to tfidf vector

compare(a,b):
	"Find Cosine similarity between 2 columns of a and b dataframe  Code any be altered to include other similarity "

Main function to find similarity among columns and tell which columns can be used to combine 2 tables



In skewkurt.py

skewness(dataset,col):
    "To Calculate the skewness of a given data For normal distribute data skewness = 0 , Skewness > 0 more weight the left tail and less weight in right tail "

kurtosis(dataset,col,ty):
    "To calculate Kurtosis of a data set ty can be fisher or pearson"


In timeseries.py:
decompose(df,col,freq):
    "To plot the decomposition graphs "
freq(df,col,max1):
    "To find the required freq for the decompostion "
lmtestcheck(df,col,max1):
    "To perform and LM test for autocorrelation and find significant lags . 1 to determine a significant lag and 0 to determine insignificant lag  "
checkdb(df,col):
    " It tells whether the Data is serially correlated or not "
check(df,col):
    "To check whether a given series is Periodic or not using AutoCorrelation function :"


In Primarykey.py:
    primarykey(dataset):
    "It is used to find a primary key in a given dataset "

In Preparation.py:
timestamp(dataset,col):
	"Find the range of time stamps of any given columns "