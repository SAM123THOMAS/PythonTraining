from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

list_urls=["https://www.moneycontrol.com/india/stockpricequote/refineries/bharatpetroleumcorporation/BPC",
           "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI",
           "https://www.moneycontrol.com/india/stockpricequote/finance-investments/hdfcassetmanagementcompany/HAM02",
           "https://www.moneycontrol.com/india/stockpricequote/steel-sponge-iron/lloydsmetalsenergy/LME",
           "https://www.moneycontrol.com/india/stockpricequote/chemicals/upl/UP04"]

driver_path="geckodriver.exe"

service = Service(driver_path)
driver = webdriver.Firefox(service=service)
driver.maximize_window()

for site in  list_urls:

    # Navigating into the URL
    driver.get(site)
    # Print title
    print("Navigating to", driver.title)
    chartElement=driver.find_element(By.ID,"advchart")
    driver.refresh()

      #Taking Element Ss

    driver.implicitly_wait(5)
    time.sleep(5)
    name=site.split("/")[-1]

    chartElement.screenshot("AdvancedGraph_"+name+".png")


# Putting delay to close
time.sleep(10)
driver.quit()

