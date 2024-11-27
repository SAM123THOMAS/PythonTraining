import requests
from bs4 import BeautifulSoup

url="https://www.w3schools.com/html/"

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
# header=soup.find(id='main')
# print(header.text.strip())

header=soup.find(id='getdiploma')
print(header.text.strip())