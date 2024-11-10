import pandas as pd
data1={
    'Name':["Sam","Thomas","Abraham","Ligin"],
    'Age':[23,25,26,21],
    'Birth City':["Tvla","tvm", "chennai","Vennikulam"]
}
data2={
    'Name':["Sam","Thomas","Abraham"],
    'Work Experience':[2,9,6],
    'Work City':["Goa","America", "Russia"]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

df3=pd.merge(df1,df2,on="Name",how="left")
print(df1)
print(df2)
print("***************************")
print(df3)
print("***************************")

df3.loc[df3["Name"]=="Ligin","Work City"]="America"
#df3["Work City"].fillna("America",inplace=True)
print("\n########################################")
print(df3)
print("##########################################")


def fn_average(ar_df3):
    average=ar_df3["Work Experience"].mean(skipna=True)
    print("Average: ",average)
    return average

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#df3["Work Experience"].fillna(fn_average(df3),inplace=True)
df3.loc[df3["Name"]=="Ligin","Work Experience"]=fn_average(df3)
print(df3)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

df3.to_csv(r"D:\PythonTraining\Daily\DAY12\test_output.csv",index=False)

#Apply
def lower_fndemo(val):
    return val.lower()

df3['Work City']=df3['Work City'].apply(lower_fndemo)
def even_creation(num):
    print(num)
    if num%2==0:
        val= True
    else:
        val= False
    return val

#df3["is Even"]=True

df3["is Even"]=df3['Work Experience'].apply(even_creation)




print("\n(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))")
print(df3)
print("(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))")