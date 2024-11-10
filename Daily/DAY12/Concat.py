import pandas as pd
import numpy as np
sample1 ={
"Name":['Amal','Bob','Cat'],
"Age":[21,22,23],
"Place":['TVLA','TVM','KOC']
}

df1=pd.DataFrame(sample1)
print(df1)

sample2 ={
"Name":['Den','Elf','Fin'],
"Age":[24,25,26],
"Place":['COC','BLR','KKD']
}
df2=pd.DataFrame(sample2)
print(df2)


df3=pd.concat([df1,df2],ignore_index=True)
print("**************************")
print(df3)
print("**************************")
#df4=df3.replace("E","T")


#df3.loc[2,'Place']="Chennai"
#print(df3)

df3.loc[df3['Name']=="Cat",'Place']="Mumbai"
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(df3)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#NaN
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
df3.loc[df3['Name']=="Cat",'Place']=np.nan
print(df3)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
df3.fillna("Kerala",inplace=True)
print("Count**Count***Count***Count***")
print(df3['Place'].value_counts())
print("Count**Count***Count***Count***")
print(df3)
