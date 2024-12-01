from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Geckodriver file path
driver_path = r'geckodriver.exe'

service = Service(driver_path)
driver = webdriver.Firefox(service=service)

# Navigating into the URL
driver.get("https://github.com/login")

print("In page: ",driver.title)


#Selections

InputUsername=driver.find_element(By.CLASS_NAME,"js-login-field")
InputPassword=driver.find_element(By.CLASS_NAME,"js-password-field")
EnterKeyInput=driver.find_element(By.CLASS_NAME,"js-sign-in-button")

InputUsername.send_keys("Student")
InputPassword.send_keys("Student@123")
#EnterKeyInput.click()
driver.implicitly_wait(5)
# Putting delay to close
time.sleep(10)
driver.quit()
