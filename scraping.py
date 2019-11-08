# usr/bin/python3
# Importing packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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


pagination_list = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'pagination')))
current_page = pagination_list.find_element_by_class_name('active')
next_page = current_page.find_element_by_xpath(".//following-sibling::li")
next_page_link = next_page.find_element_by_xpath('.//a').get_attribute('href')
next_page_class = next_page.get_attribute('class')
while next_page_link is not None:
    print(current_page.text)
    list_results = wait.until(
        EC.presence_of_element_located((By.XPATH, '//ul[@id="milieu"]')))
    options = list_results.find_elements_by_tag_name("li")

    links = []
    for option in options:
        links.append(option.find_element_by_xpath(
            './/h6/a').get_attribute('href'))

    for link in links:
        driver.get(link)
        # SAVE DATA
        driver.back()

    # DOM changed so try to get back current page and next page
    pagination_list = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'pagination')))
    current_page = pagination_list.find_element_by_class_name('active')
    next_page = current_page.find_element_by_xpath(".//following-sibling::li")

    # Link of next page is javascript action
    # For now: it seems to go back to page 1 and it loops endlessly on page 1
    next_page.find_element_by_xpath('.//a').click()

    # Is supposed to update current page and next page once we land one page 2, etc...
    pagination_list = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'pagination')))
    current_page = pagination_list.find_element_by_class_name('active')
    next_page = current_page.find_element_by_xpath("//following-sibling::li")
    next_page_class = next_page.get_attribute('class')
