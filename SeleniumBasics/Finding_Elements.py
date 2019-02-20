""""
Write a Program to find all the links in a web page
"""

from selenium import webdriver
import time

class Finding_All_Links:

        def findingLinks(self):

            driver = webdriver.Chrome()
            driver.get("https://www.google.com/")
            driver.maximize_window()
            element = driver.find_elements_by_xpath("//a")
            print(type(element))
            print(element)


for ele in element:
    url = ele.get_attribute("href")
print(url)

selenium = Finding_All_Links()
selenium.findingLinks()