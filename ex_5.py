"""
a)	Join the below 2 dataframes along ROWS and print.
b)	Join the below 2 dataframes along Columns and print.

Given_dict1 = {'name': ['Karthik', 'Raman', 'Ananth', ‘Raman’],
              'age' : [32, 35, 38, 23],
              'occupation' : ['engineer', 'doctor', 'accountant', ‘student’]}

Given_dict2 = {'name': ['Kayal', 'Rasi', 'Lakshmi', ‘Harini’],
              'age' : [30, 25, 28, 13],
              'occupation' : ['engineer', 'Housewife', 'doctor', ‘student’]}
"""
import pandas as pd
Given_dict1 = {'name': ['Karthik', 'Raman', 'Ananth','Raman' ],
              'age' : [32, 35, 38, 23],
              'occupation' : ['engineer', 'doctor', 'accountant', 'student']}

Given_dict2 = {'name': ['Kayal', 'Rasi', 'Lakshmi', 'Harini'],
              'age' : [30, 25, 28, 13],
              'occupation' : ['engineer', 'Housewife', 'doctor', 'student']}

df1=pd.DataFrame(Given_dict1)
df2=pd.DataFrame(Given_dict2)
print("Join the below 2 dataframes along ROWS and print.")
df=pd.concat([df1,df2],axis=1,join='inner')
print(df)
print(" ")
print("Join the below 2 dataframes along Columns and print.")
df=pd.concat([df1,df2],axis=0,join='outer')
print(df)
