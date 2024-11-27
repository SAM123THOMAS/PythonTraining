import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

#url="https://www.worldometers.info/world-population/population-by-country/"
url="https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

tables=soup.find('table')
rows=tables.find_all('tr')
master_List=[]

for row in rows:
    cells=row.find_all('td')
    data=[cell.text.strip() for cell in cells]
    master_List.append(data)

df=pd.DataFrame(master_List,columns=['Country/Territory','Population 2022','Population 2023','Change','Region','SubRegion'])
df=df.dropna()

filename="Population.csv"
df.to_csv(filename,index=False)
