import pandas as pd
import numpy as np


def rep(dataframe, col, choice, value):
	"Tells about all the rows with which has an empty value for a particular column with an option to add / alter the values indicating empty values eg . NULL , NaN ,  , unknown etc and also allows a person to replace a given value choice is used to tell your choice whether to replace the value or not , value to enter a value you want to replace it with   "
	a = []
	print '****'
	maintainchar = ['unknown', 'Unknown', 'Null', 'null', '', '\0', np.nan]
	maintainint = [np.nan]
	count = 0
	k = -1
	reg = 0
	###print 'Do you want to replace value with something '
	##choice = True  ## input choice here
	##value=0 ## Enter the value here
	if(choice==False):

		if (dataframe[col].dtype == 'object'):
			##print '1'
			##dataframe[col].fillna(value, inplace=True)
			for i in dataframe[col].tolist():
				count=count+1
				if (i in maintainchar or i==np.nan):
					print 'Record No ', count, 'has  a problem'
					reg = reg + 1
		else:
			##dataframe[col].fillna(value, inplace=True)
			for i in np.asarray(dataframe[col].tolist()):
				count = count + 1
				##print '4',i

				if (i in maintainint or  np.isnan(i)):
					print 'Record No ', count, 'has  a problem'
					reg = reg + 1
		return reg
	else:
		li = []
		##dataframe[col].fillna(value,inplace=True)
		if (dataframe[col].dtype == 'object'):
			for i in dataframe[col].tolist():
				##k=k+1
				##print '2'
				count = count + 1
				if (i in maintainchar):
					print 'Record No ', count, 'has  a problem'
					li.append(value)
					##dataframe.iloc[k][col] = value
					reg = reg + 1
				else:
					li.append(i)
		else:
			li = []
			##dataframe[col].fillna(value, inplace=True)
			sd = np.asarray(dataframe[col].tolist())
			for i in sd:
				count = count + 1
				##print i
				##k = k + 1
				if (i in maintainint or np.isnan(i)):
					print 'Record No ', count, 'has  a problem'
					##dataframe.loc[k,col] = value
					li.append(value)
					reg = reg + 1

				else:

					li.append(i)

		dataframe[col].update(pd.Series(li))

		return dataframe


