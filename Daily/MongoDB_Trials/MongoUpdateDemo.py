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

    docid="673835d6211261f70d407516"
    query = {"_id":ObjectId(docid)}
    update={"$set":{"name":"Sam Thomas","age":27,"city":"Kottayam" ,"Best Season":["Winter","Spring"]}}
    result=collection.update_one(query,update)
    
    results=collection.find()

    if(result.matched_count>0):
        print("there was a match, document has been found")


except Exception as e:
    print(e)


result_list=list(results)

df=pd.DataFrame(result_list)
print(df.head(20))
#print(df.columns)

client.close()


