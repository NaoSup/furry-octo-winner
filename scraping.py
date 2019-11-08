# usr/bin/python3
# Importing packages
from selenium import webdriver
import pandas as pd


driver = webdriver.Chrome(
    '/Users/dineshsalhotra/Documents/Formations/Automatisation Informatique/furry-octo-winner')
driver.get('https://www.myfrenchstartup.com/fr/')
