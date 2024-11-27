import requests
from bs4 import BeautifulSoup

url="https://example.com"

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

h1_tag=soup.find('h1')
if(h1_tag):
    print(h1_tag.text)
links=soup.find_all('a')
for link in links:
    href=link.get('href')
    print(href)


p_tags=soup.find_all('p')
for p_tag in p_tags:
    print(p_tag.text)