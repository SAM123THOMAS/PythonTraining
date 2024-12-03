from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver_path="geckodriver.exe"

service = Service(driver_path)
driver = webdriver.Firefox(service=service)
driver.maximize_window()

# Navigating into the URL
driver.get("https://www.wikipedia.org/")
driver.implicitly_wait(3)

#get xpath of search box
search_box=driver.find_element(By.XPATH,"//input[@id='searchInput']")
search_box.send_keys("India")


search_btn=driver.find_element(By.XPATH,"""//*[@id="search-form"]/fieldset/button/i""")
search_btn.click()
driver.implicitly_wait(5)

heading=driver.find_element(By.XPATH,"//h2[contains(text(),'Etymology')]")

print(heading)

driver.quit()