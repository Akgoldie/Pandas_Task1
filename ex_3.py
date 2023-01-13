"""convert the below dictionary into corresponding dataframe and display it.
Given_dict = { 'name' : [ 'Karthik' ,  'Raman' ,  'Ananth' , 'Raman'],
 'age'  : [32, 35, 38, 23],
 'occupation'  : [ 'engineer' ,  'doctor' ,  'accountant' , 'student']}"""

import pandas as pd
Given_dict = { 'name' : [ 'Karthik' ,  'Raman' ,  'Ananth' , 'Raman'],
 'age'  : [32, 35, 38, 23],
 'occupation'  : [ 'engineer' ,  'doctor' ,  'accountant' , 'student']}

data=pd.DataFrame(Given_dict)
print(data)