import requests
from bs4 import BeautifulSoup

url="https://realpython.com"

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

titles=soup.find_all(class_="card-title")
for tile in titles:
    print(tile.text)