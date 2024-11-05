import pandas as pd

dictio={
    "Name":['Sam','Ligin'],
    "Age":['23','21'],
    "From":['Thiruvalla','Mallappally']
       }
df=pd.DataFrame(dictio,index=['RANK1','RANK2'])
#print(df)

for row_index, row_value in df.iterrows():
    print('-------------------------')
    print("row_index is:",row_index)
    print("row_value is:\n",row_value)
print("##############################")
for col_name,col_value in df.iteritems():
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print('Column Name is::', col_name)
    print("Column Values are::")
    print(col_value)
