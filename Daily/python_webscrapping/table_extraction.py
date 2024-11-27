import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.worldometers.info/world-population/"

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

tables=soup.find('table')
rows=tables.find_all('tr')
master_List=[]

for row in rows:
    cells=row.find_all('td')
    data=[cell.text.strip() for cell in cells]
    master_List.append(data)
print(pd.DataFrame(master_List))