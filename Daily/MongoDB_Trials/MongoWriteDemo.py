from pymongo import MongoClient
import pandas as pd


connection_string=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client=MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("connected to mongo atlassuccess")

    #connect to mongo cluster

    db=client['ust_live_quiz']

    #access a collection

    collection=db["basic_collection_test"]

    sample_data={
        "name":"Sam",
        "work location":"TVM",
        "city":"kerala",
        "Year":"2024"
    }

    collection.insert_one(sample_data)
    print("insert successfull")
    results=collection.find()
except Exception as e:
    print(e)


result_list=list(results)

df=pd.DataFrame(result_list)
print(df.head(20))
#print(df.columns)

client.close()


