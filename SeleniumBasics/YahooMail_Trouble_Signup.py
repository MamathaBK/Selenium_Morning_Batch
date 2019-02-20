from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class YahooTrouble_Signup:

    def Trouble_Signup(self):

        Base_Url = "https://www.yahoomail.com"
        driver = webdriver.Chrome()
        driver.get(Base_Url)
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,"Trouble Signing in?").click()
        driver.back()
        driver.find_element(By.PARTIAL_LINK_TEXT,"Trouble").click()
        driver.back()
        time.sleep(5)

selenium = YahooTrouble_Signup()
selenium.Trouble_Signup()