import requests

url="https://httpbin.org/headers"
headers={"Custom-Header":"Han's value"}
response=requests.get(url,headers=headers)
print(response)
print(type(response))
print(response.headers)
print(response.json())