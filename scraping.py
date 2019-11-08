# usr/bin/python3
# Importing packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome(
    '../chromedriver')
wait = WebDriverWait(driver, 10)
driver.get('https://www.myfrenchstartup.com/fr/connexion')


driver.find_element_by_name('login_connect').send_keys(
    'capikif560@mailhub24.com')
driver.find_element_by_name('pwd').send_keys('E7qt4Sqg@np3MW4')
driver.find_element_by_xpath('//button[@type=\'submit\']').click()
driver.get(
    'https://www.myfrenchstartup.com/fr/liste-investisseurs')


results = driver.find_element_by_xpath('//div[@id=\'bloc_resultat\']')
list_results = wait.until(
    EC.presence_of_element_located((By.XPATH, '//ul[@id="milieu"]')))
options = list_results.find_elements_by_tag_name("li")
for option in options:
    link = option.find_element_by_xpath('//h6/a')
    link.click()
# items = list3.find_elements_by_tag_name("li")
# for item in items:
#     item
#     print(item)
# # list = driver.find_element_by_xpath(
# #     '//ul[@id=\'milieu\']')
# driver.close()
