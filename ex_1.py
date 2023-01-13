#Using the given series, Print the series with odd indexes only by using Pandas.
#X_List = [7, 10, 22, 42, 55]

import pandas as pd
a=[7,10,22,42,55]
data=pd.Series(a,index=[1,3,5,7,9])
print(data)
