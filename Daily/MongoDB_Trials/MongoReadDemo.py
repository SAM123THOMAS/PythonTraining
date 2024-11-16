from pymongo import MongoClient
import pandas as pd


connection_string=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client=MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("connected to mongo atlassuccess")

    #connect to mongo cluster

    db=client['sample_mflix']

    #access a collection

    collection=db["movies"]

    #query collection
    results=collection.find().limit(5)
    # for doc in results:
    #     print(doc)
    #     break
    result_list=list(results)

    df=pd.DataFrame(result_list)
    print(df.head())
    print(df.columns)

except Exception as e:
    print(e)

finally:
    client.close()


