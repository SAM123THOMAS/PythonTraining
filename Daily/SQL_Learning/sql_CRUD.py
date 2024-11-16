import sqlite3
connection=sqlite3.connect(r'D:\PythonTraining\Daily\SQL_Learning\Chinook_Sqlite.sqlite')
cursor=connection.cursor()




#CRUD - >Create, Read, Update, Delete

#Create Operations
#CustomerID,FirstName, LstName, Company, Email, Country, Phone

# new_customer =(60, 'Rajiv', 'RR','ABC','sa@gmail.com','IND')
# #(CustomerID, FirstName, LastName, Company, Email, Country, Phone)

# cursor.execute(
#     """
#     INSERT INTO Customer(CustomerId, FirstName, LastName,
#     Company, Email, Country) VALUES(?,?,?,?,?,?)
    
#     """, new_customer
# )
# connection.commit()
# print("New customer added")

#Read the customer that u just wrote to database

# cursor.execute("SELECT * FROM Customer WHERE CustomerID=60")

# data=cursor.fetchone()
# print(data)

#Change the comany and email id

# customer_id=60
# new_email='ra@ust.com'


# cursor.execute(
#     """
#     UPDATE Customer
#     SET Email=?, Company=?
#     WHERE CustomerId=?
#     """,(new_email,'UST',customer_id)
# )
# connection.commit()
# print("Customer Updated")



#DELETE
cursor.execute(
    """
    DELETE FROM Customer WHERE CustomerID=60
    """
)

cursor.execute("SELECT * FROM Customer WHERE CustomerID=60")
data=cursor.fetchall()
for row in data:
    print(row)


desc=cursor.description
cols=[col[0] for col in desc]
print(cols)

    
