from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os
import streamlit as st

movieName = st.text_input("Enter movie to search:")
option = st.selectbox(
    "Select operation",
    ("Rating","Director","Plot"),
)

data= "Test data"
movieDetails = {}
def movieExtraction():
            driver_path=os.getcwd()+ "\Daily\SeleniumTraining\geckodriver.exe"
            service = Service(driver_path)
            driver = webdriver.Firefox(service=service)
            driver.maximize_window()
            # Navigating into the URL
            driver.get("https://www.imdb.com/")
            # Print title
            print("Navigating to", driver.title)

            searchElement=driver.find_element(By.XPATH,"""//input[@id="suggestion-search"]""")
            searchElement.send_keys(movieName)
            searchElement.send_keys(Keys.ENTER)

            time.sleep(5)

            movieClick=driver.find_element(By.CLASS_NAME,"ipc-metadata-list-summary-item__t")
            movieClick.click()
            time.sleep(5)
            titleFind=driver.find_element(By.XPATH,"//h1[@data-testid='hero__pageTitle']//span")
            ratingSelector=driver.find_element(By.XPATH,"//div[@data-testid='hero-rating-bar__aggregate-rating__score']//span")
            directorDriver=driver.find_element(By.XPATH,"//li[@data-testid='title-pc-principal-credit']//a")
            plotFinder=driver.find_element(By.XPATH,"//p[@data-testid='plot']//span[@data-testid='plot-xl']")
            
            movieDetails = {'Title' : titleFind.text,
                         'Rating' : ratingSelector.text+"/10",
                         'Director' : directorDriver.text,
                         'Plot' : plotFinder.text}
  
            driver.quit()
            return movieDetails.get('Title') + " -- " + option + ":" + movieDetails.get(option)



if(st.button("Search", type="primary")):
    if(len(movieName)>0 and len(option)>0):
        st.write("Creating the results for movie :", movieName )
        data = movieExtraction()
        st.write(":green[" + data + "]")
    else:
        st.write(":red[Invalid inputs,Please Provide both inputs or options!!]")