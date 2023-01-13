#Generate the series of dates from 1st November 2022 to 25th November 2022.

import pandas as pd
list=pd.date_range(start='11/01/2022',end='11/25/2022',freq='D')
data=pd.Series(list)
print(data)