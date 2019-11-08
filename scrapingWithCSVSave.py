# usr/bin/python3
# Importing packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import csv

try:
    os.remove('Scraping data et Analytique.csv')
except OSError:
    pass

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
links = []
investisseursName = []
# get labels first

for option in options:
    links.append(option.find_element_by_xpath(
        './/h6/a').get_attribute('href'))
    investisseursName.append(option.find_element_by_xpath(
        './/h6/a').text)
driver.get(links[0])
starUpTab = wait.until(
    EC.presence_of_element_located((By.ID, 'example')))

starUpTabElementsLabels = starUpTab.find_element_by_tag_name('thead')
starUpListLabelsrow = starUpTabElementsLabels.find_element_by_tag_name(
    'tr')
starUpListLabels = starUpListLabelsrow.find_elements_by_tag_name('th')
lables = []
for starUpLabel in starUpListLabels:
    lables.append(starUpLabel.text)
lables.append('Investisseurs')
with open('Scraping data et Analytique.csv', 'a+') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(lables)

for i, link in enumerate(links):
    driver.get(link)
    starUpTab = wait.until(
        EC.presence_of_element_located((By.ID, 'example')))

    starUpTabElements = starUpTab.find_element_by_tag_name('tbody')
    starUpList = starUpTabElements.find_elements_by_tag_name('tr')

    for starUpTabElement in starUpList:
        startUpInfo = []
        #     # get name of the startUp
        startUpInfo.append(starUpTabElement.find_element_by_xpath(
            '//div[@class="media-left"]//a').text)
        startUpInfo.append(starUpTabElement.find_element_by_xpath(
            '//td/span').text)
        startUpInfo.append(starUpTabElement.find_element_by_xpath(
            '//td[3]').text)
        startUpInfo.append(investisseursName[i])
        with open('Scraping data et Analytique.csv', 'a+') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(startUpInfo)
    driver.back()
