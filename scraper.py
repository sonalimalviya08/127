from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("C:/Users/home/Desktop/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
    print("scrapping")
     

        # Find all elements on the page and click to move to the next page
       
scrape()
# Calling Method    


# Define Header


# Define pandas DataFrame   


# Convert to CSV
