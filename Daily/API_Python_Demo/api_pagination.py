import requests
url="https://jsonplaceholder.typicode.com/posts"
params ={"_page":1,"_limit":5}
combine_response=[]

for i in range(10):
    params ={"_page":i}


    response=requests.get(url,params)
    combine_response+=response.json()
    print("\n******************************\n")
    #print(response)
    #print(response.headers)
    print(combine_response)
    #print("\n\n",len(response.json()))