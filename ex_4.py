"""Using the above dictionary,
a)	print the dataframe in the ascending order of Name
b)	print the dataframe in the ascending order of Name, Occupation
c)	print the dataframe only with column ‘name’
d)	Print the dataframe only with first 2 rows only
e)	Print the dataframe only with ‘age > 30’
"""

import pandas as pd
Given_dict = { 'name' : [ 'Karthik' ,  'Raman' ,  'Ananth' , 'Raman'],
 'age'  : [32, 35, 38, 23],
 'occupation'  : [ 'engineer' ,  'doctor' ,  'accountant' , 'student']}

data=pd.DataFrame(Given_dict)
print("print the dataframe in the ascending order of Name")
print(data.sort_values('name'))
print(" ")
print("print the dataframe in the ascending order of Name, Occupation")
print(data.sort_values(['name','occupation']))
print(" ")
print("print the dataframe only with column ‘name’")
print(data['name'])
print(" ")
print("Print the dataframe only with first 2 rows only")
print(data.head(2))
print(" ")
print("Print the dataframe only with ‘age > 30’")
print(data.loc[data['age']>30])