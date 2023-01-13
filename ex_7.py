"""
Read the student.excel file by using Pandas
a)	All Rows
b)	First 5 rows
c)	Last 5 rows
d)	Display Dimensions or Shape of the dataframe
e)	Display Number of columns and rows
f)	Print only column names
g)	Print student details who scored > 50 and gender = ‘female’.
"""
import  pandas as pd

data=pd.read_excel("C:\\Users\\91962\\Downloads\\student_excel.xlsx")
df=pd.DataFrame(data)
print(" ")
print("a. print the All Rows")
print(df.to_string())
print(" ")
print("b. print the First 5 rows")
print(df.head())
print(" ")
print("c. print Last 5 rows")
print(df.tail())
print(" ")
print("d. print the Display Dimensions or Shape of the dataframe")
print(df.ndim)
print(" ")
print("e. print the Display Number of columns and rows")
print(df.shape)
print(" ")
print("f. print the Print only column names")
print(df.columns)
print(" ")
print("g. print the Print student details who scored > 50 and gender = ‘male’")
print((df.loc([df['mark']>50] ) & (df['gender']=='female')))
"""df_marks=df.loc[df['mark']>50]
#print(df_marks)
df_gender=df_marks.loc[df['gender']=="male"]
print(df_gender)

"""
