from selenium import webdriver
import time

class Acti_Time_Login:

    def Verify_Login(self):

        base_url = "www.gmail.com"
        driver = webdriver.Chrome()
        driver.get(base_url)
        username = driver.find_element_by_xpath('//input[@type="email"]')
        driver.find_element_by_xpath().send_keys(Keys.ENTER)
        username.send_keys(Keys.CONTROL + 'a')
        usermame.send_keys(Keys.DELETE)