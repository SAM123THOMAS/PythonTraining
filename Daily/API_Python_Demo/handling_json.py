import requests
import json
url="https://api.coingecko.com/api/v3/simple/price"
params={
    "ids":"bitcoin,ethereum","vs_currencies":"inr"
}

response=requests.get(url,params)
print(response.json())
#print(response.json(parse_int="inr"))

final_Value=response.json()["ethereum"]["inr"]
print(final_Value)
