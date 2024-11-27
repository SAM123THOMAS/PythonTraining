import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.bbc.com/news"

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
NewsList=[]
h2_tags=soup.find_all(class_="sc-8ea7699c-3")
for h2_tag in h2_tags:
    data=h2_tag.text
    NewsList.append(data)

df=pd.DataFrame(NewsList,columns=['Trending News']).drop(index=0)
filename="NewsCard.csv"
df.to_csv(filename,index=False)

