import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://unsplash.com/s/photos/nature"

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

images=soup.find_all("img",{"srcset":True})
print(len(images))
count=1
for img in images:
    print("image source: ",img.get("src"))
    image_url=img.get("src")
    img_data=requests.get(image_url).content
    img_path="Image"+str(count)+".jpg"
    with open(img_path,"wb") as img_file_handler:
        img_file_handler.write(img_data)
    count+=1


# image_url=images[-1]
# image_url=image_url['src']
# print(image_url)

# img_data=requests.get(image_url).content
# img_path="sample_image.jpg"

# with open(img_path,"wb") as img_file_handler:
#     img_file_handler.write(img_data)