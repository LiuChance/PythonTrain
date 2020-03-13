import pandas as pd
import numpy as np


s = pd.Series(np.arange(10), index=list('abcdefghij'))
print('创建s: \n',s,'\n---------')
