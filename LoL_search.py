# Search for an user on na.op.gg
# Author: Yuxiao Sean Ran
# Date: 7/2/2019

# import packages
from selenium import webdriver
import time
import sys

# parse username
username = ""
for i in range(1, len(sys.argv)):
    username += sys.argv[i]
    username += " "
username = username[0 : len(username) - 1]

url = "https://na.op.gg/"

driver = webdriver.Chrome(r"C:\Users\sran\Downloads\chromedriver.exe")

driver.get(url)

# search for user
driver.find_element_by_name("userName").send_keys(username)
driver.find_element_by_class_name("summoner-search-form__button").click()

driver.find_elements_by_css_selector("a.Button")[-1].click()

time.sleep(10)

driver.quit()
