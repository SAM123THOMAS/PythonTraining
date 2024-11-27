import csv
import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com"

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

quotes=soup.select(".quote .text")
authors=soup.select(".quote .author")

filename="Sample.txt"
with open(filename,'a') as file:
    writer = csv.writer(file)
    for each_quote, each_author in zip(quotes,authors):
        text_s=each_quote.text," - "+each_author.text
        writer.writerow(text_s)
file.close


    
        
