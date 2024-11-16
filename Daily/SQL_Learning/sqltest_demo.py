import sqlite3
connection=sqlite3.connect(r'D:\PythonTraining\Daily\SQL_Learning\Chinook_Sqlite.sqlite')
cursor=connection.cursor()
print(cursor)

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables=cursor.fetchall()
# for table in tables:
#     print(table)

cursor.execute("SELECT * FROM 'Album' limit 10")
data=cursor.fetchall()
for row in data:
    print("\n", row)


desc=cursor.description
cols=[col[0] for col in desc]
print(cols)