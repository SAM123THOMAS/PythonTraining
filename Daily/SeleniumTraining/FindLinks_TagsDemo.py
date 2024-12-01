from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver_path="geckodriver.exe"
service=Service(driver_path)
driver=webdriver.Firefox(service=service)
driver.get("https://en.wikipedia.org/wiki/India")
#tag_selection=driver.find_elements(By.TAG_NAME,"a")
links_list = driver.find_elements(By.TAG_NAME,"a")
# print(links_list)

for lnk in links_list:
    print(lnk.text, " - ", lnk.get_attribute("href"))

driver.implicitly_wait(5)

# Putting delay to close
time.sleep(10)
driver.quit()