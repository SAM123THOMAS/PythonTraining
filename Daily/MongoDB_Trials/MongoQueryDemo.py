from pymongo import MongoClient
import pandas as pd
from bson.objectid import ObjectId


connection_string=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client=MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("connected to mongo atlassuccess")

    #connect to mongo cluster

    db=client['ust_live_quiz']

    #access a collection

    collection=db["basic_collection_test"]
 #query ollection
    query={"age":{"$gt":20}}
    results=collection.find(query)
    


except Exception as e:
    print(e)


result_list=list(results)

df=pd.DataFrame(result_list)
print(df.head(20))
#print(df.columns)

client.close()


