from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path="geckodriver.exe"

service = Service(driver_path)
driver = webdriver.Firefox(service=service)
driver.maximize_window()

# Navigating into the URL
driver.get("https://en.wikipedia.org/wiki/India")
# Print title
print("Navigating to", driver.title)




link= driver.find_element(By.LINK_TEXT,"Harappa")

print(link.text, " - ", link.get_attribute("href"))

driver.get(link.get_attribute("href"))

driver.implicitly_wait(5)
driver.back()
driver.implicitly_wait(5)
driver.forward()

# Putting delay to close
time.sleep(10)
driver.quit()
