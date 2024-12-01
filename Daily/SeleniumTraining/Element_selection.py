from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver_path="geckodriver.exe"
service=Service(driver_path)
driver=webdriver.Firefox(service=service)
driver.get("https://www.duckduckgo.com/")

search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Testing")
search_box.send_keys(Keys.ENTER)
#Selenium specific instruction
#driver.implicitly_wait(15)

print("Title:", driver.title)

#Program specific instruction
time.sleep(10)

driver.quit()



