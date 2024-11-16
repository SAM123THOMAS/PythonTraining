import sqlite3
import pandas as pd
connection=sqlite3.connect(r'D:\PythonTraining\Daily\SQL_Learning\Chinook_Sqlite.sqlite')
cursor=connection.cursor()

# query="""
# SELECT * FROM Customer limit 10
# """








#1.Determine the total sales(sum of total) for each country in the invoices table

# query="""
# SELECT BillingCountry,SUM(Total) As TotalSales 
# FROM Invoice
# GROUP BY BillingCountry

# """

# df_customers=pd.read_sql_query(query,connection)
# print(df_customers)


query="""
SELECT * 
FROM Invoice
"""

df_customers=pd.read_sql_query(query,connection)
df=df_customers.groupby("BillingCountry")["Total"].sum().reset_index()
print(df)









connection.close()