"""
Create a menu driven program tp take a movie name from the user and get it's rating using selenium from an online source(IMDB/Rotten Tomatos etc) and other details

Menu should have option for getting rating, writing all ratings to a file
When user presses for quit the program, write all the movies and ratings that the user had asked in the session to a file.

Tips:
1. Create component wise, for eg. first create a selenium program to do this and then make it menu driven
2.Later write to file
3.Store all searches in a container (list/dict) and then write to file
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os
driver_path=os.getcwd()+ "\Daily\SeleniumTraining\geckodriver.exe"
input_val=4
list_movies=[]
while(input_val!=3):
    try:
        print("*************************************************\n1.Get Rating\n2.Writing Rating\n3.Exit\n*************************************************")

        input_val=int(input("Enter ur choice:"))
        
        if(input_val==1):
            movie_name=input("Enter a movie name: ")  
            service = Service(driver_path)
            driver = webdriver.Firefox(service=service)
            driver.maximize_window()

            # Navigating into the URL
            driver.get("https://www.imdb.com/")
            # Print title
            print("Navigating to", driver.title)

            searchElement=driver.find_element(By.XPATH,"""//input[@id="suggestion-search"]""")
            searchElement.send_keys(movie_name)
            searchElement.send_keys(Keys.ENTER)

            time.sleep(5)

            movieClick=driver.find_element(By.CLASS_NAME,"ipc-metadata-list-summary-item__t")
            movieClick.click()
            time.sleep(5)
            rating=driver.find_element(By.CLASS_NAME,"sc-d541859f-0").text

            print(rating)

            
            list_movies.append([movie_name,rating.split("\n")[0],rating.split("\n")[2]])
            driver.quit()

            
        elif(input_val==2):
            df=pd.DataFrame(list_movies,columns=["Movie Name","Rating","Rating from Number"])
            df.to_csv(os.getcwd()+ "\Daily\SeleniumTraining\Movies.csv",index=False)
    except:
        print("Error")


df=pd.DataFrame(list_movies,columns=["Movie Name","Rating","Rating from Number"])
df.to_csv(os.getcwd()+ "\Daily\SeleniumTraining\Movies.csv",index=False)


