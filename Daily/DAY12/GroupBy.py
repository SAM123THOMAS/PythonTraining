import pandas as pd
import numpy as np

data1={
    'Number 1':[1,2,3,4],
    'Number 2':[2,2,2,2],
    'Number 3':[2,2,2,3]
}

df1=pd.DataFrame(data1)
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(df1)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

df1.index=['Customer A','Customer A','Customer B','Customer B']
df1.columns=['Product A','Product B','Product C']

print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(df1)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

df1['Customer']=df1.index
print("\n####################################################")
print(df1)
print("####################################################")

df2=df1.groupby(['Customer']).mean()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(df2)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

df3=df1.groupby(['Customer']).agg({'Product A':sum,'Product B':np.mean,'Product C':np.median})

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(df3)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")