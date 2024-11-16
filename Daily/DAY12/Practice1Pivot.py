#1.create a pivot table showing total sales per store
#2.create a pivot table showing total sales per region
import pandas as pd
data={
    'Store':['Store1','Store1','Store2','Store2','Store3','Store3','Store4','Store5'],
    'Region':['North','North','South','South','East','East','North','South'],
    'Sales':[200,150,300,250,400,350,100,200]
}
df=pd.DataFrame(data)
print(df)

#Creation of pivot table with total sales per store
df_grpStore=df.groupby('Store')['Sales'].sum().reset_index()
print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(df_grpStore)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#Creation of pivot table with total sales per Region
df_grpRegion=df.groupby('Region')['Sales'].sum().reset_index()
print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(df_grpRegion)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

#Create new column Region_Sales and place values accordingly
RegionSales_df=df.groupby('Region').agg({'Sales':sum}).reset_index()
print("\n################################################################")
df_merged=pd.merge(df,RegionSales_df,on="Region",how="left",suffixes=("_Store","_Region"))
print(df_merged)
print("################################################################")





#% of each store in region

df_latestMerged=pd.merge(df_merged,df_grpStore,on="Store",how="left")

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(df_latestMerged)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

def percentage_fn(val):
    return (val['Sales']/val['Sales_Region']*100)

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
df_latestMerged["Sale_StorePercentage"]=df_latestMerged.apply(percentage_fn,axis=1)
df_latestMerged.rename(columns={"Sales":"SalesPerStore"},inplace=True)
print(df_latestMerged)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")