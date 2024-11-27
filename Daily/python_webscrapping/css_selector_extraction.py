import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com"

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

quote_object=soup.find(class_='quote')
text_object=quote_object.find(class_='text')
print(text_object.text.strip())

author_object=quote_object.find(class_='author')
print(author_object.text.strip())
