import pandas as pd 
import numpy as np
def repl(dataframe,col):
	a = []
	maintainchar = ['unknown','Unknown','Null','null','','\0',np.nan]
	maintainint = ['-','NaN','',np.nan]
	count = 0
	k=-1
	reg = 0  
	print 'Do you want to replace value with something '
	choice = False ## input choice here 
	value = 0 ## Enter the value here 
	if(choice):

		if(dataframe[col].dtype == 'object'):
			
			for i in dataframe[col].tolist():
				count = count + 1
				if(i in maintainchar):
					print 'Record No ',count ,'has  a problem'
					reg = reg + 1  
		else: 
			for i in dataframe[col].tolist():
				count = count + 1
				if(i in maintainint):
					print 'Record No ',count ,'has  a problem'
					reg = reg + 1
		return reg
	else:
		li = []
		if(dataframe[col].dtype == 'object'):
			for i in dataframe[col].tolist():
				##k=k+1
				count = count+1
				if(i in maintainchar):
					print 'Record No ',count ,'has  a problem'
					li.append(value)
					##dataframe.iloc[k][col] = value
					reg = reg + 1  
				else:
					li.append(i)			
		else: 
			li=[]
			for i in dataframe[col].tolist():
				count=count+1
				##k = k + 1
				if(i in maintainint):


					print 'Record No ',count ,'has  a problem'
					##dataframe.loc[k,col] = value
					li.append(value)
					reg = reg + 1
				else:
					li.append(i)
		dataframe[col].update(pd.Series(li))		
		
		return reg



df = pd.read_csv('bank-full.csv',';')
print df 
k = asp(df,'poutcome')
print k
print df 