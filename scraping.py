# usr/bin/python3
# Importing packages
from selenium import webdriver
import pandas as pd


driver = webdriver.Chrome(
    '/Users/dineshsalhotra/Documents/Formations/Automatisation Informatique/furry-octo-winner/chromedriver')
driver.get('https://www.myfrenchstartup.com/fr/connexion')


driver.find_element_by_name('login_connect').send_keys(
    'capikif560@mailhub24.com')
driver.find_element_by_name('pwd').send_keys('E7qt4Sqg@np3MW4')
driver.find_element_by_xpath('//button[@type=\'submit\']').click()
driver.get(
    'https://www.myfrenchstartup.com/fr/liste-investisseurs')


list3 = driver.find_element_by_xpath('//div[@id=\'bloc_resultat\']//ul')


# items = list3.find_elements_by_tag_name("li")
# for item in items:
#     item
#     print(item)
# # list = driver.find_element_by_xpath(
# #     '//ul[@id=\'milieu\']')
# driver.close()
