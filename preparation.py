import pandas as pd
import matplotlib.pyplot as pld
r = "bank.csv"## Name of the file
d = ";"## delimiter
def timestamp(dataset,col):
	"Find the range of time stamps of any given columns "
	print "Time stamp lies between", dataset[col].min(), " and ", dataset[col].max()
'''
df = pd.read_csv(r,d);
## Calculate the time stamp 
row = "a";
for row in df:
	timestamp(df,row)
'''
'''
for i in range(df[row].count()):
	for row in df:
		if(df[row].iloc[i]== "NaN" or df[row].iloc[i]=="unknown" ):
			print (i+1)," has a Not definated value at ",row,"column"
'''
