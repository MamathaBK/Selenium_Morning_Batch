from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class ScrollBy:

    def S_Example(self):
            base_url = "file:///C:/Users/Mamatha/Desktop/Practice.html"
            driver = webdriver.Chrome()
            driver.get(base_url)
            driver.maximize_window()
            driver.implicitly_wait(3)
            driver.execute_script("window.scrollBy(0,2000);")
            time.sleep(3)
            driver.execute_script("window.scrollBy(0,-1000);")
            time.sleep(3)
            # res = driver.execute_script("console.log('Hello')")
            # print(res)
            element = driver.find_element_by_id('hide-textbox')
            driver.execute_script("argument[0].window.scrollIntoView(true);", element)
            time.sleep(2)

ScrollBy().S_Example()