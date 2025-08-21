#Practice usage of numpy & pandas

import pandas as pd
import numpy as np

# 1) Simple Numpy.array 
numpy_1 = np.array([[1,2,3,],[10,20,30],[100,200,300]])  

# 2) To rember and know how to reshape the .reshape(Rows, Columns)
numpy_2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[0,0,0,0,0]]).reshape(5,3)

# 3) Simple Pandas.DataFrame and the later lists(arrays) are to give Rows & Columns (Excel Form)
pandas_1 = pd.DataFrame([[1,2,3,],[10,20,30],[100,200,300]], ['R1', "R2",'R3'], ['C1', 'C2', 'C3'])  

print(numpy_1)
print("\n",numpy_2, "\n\n", pandas_1)

# .describe used to stats info about data
# print(pandas_1.describe())

# How to Save it in csv (Excel Format)
#pandas_1.to_csv("Name.csv")

# How to read an existing csv file 
#new_file = pd.read_csv("Name.csv")