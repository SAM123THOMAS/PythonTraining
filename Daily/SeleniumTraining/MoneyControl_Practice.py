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
driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")
# Print title
print("Navigating to", driver.title)
chartElement=driver.find_element(By.ID,"advchart")

# Scrolling to the Element
Actions = ActionChains(driver)
Actions.scroll_to_element(chartElement)



#Taking Element Ss

driver.implicitly_wait(5)
time.sleep(5)

chartElement.screenshot("AdvancedGraph.png")

# Taking the page screenshot
driver.implicitly_wait(5)
time.sleep(5)
driver.save_screenshot("ChartNavigated.png")

# Putting delay to close
time.sleep(10)
driver.quit()

