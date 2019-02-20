from selenium import webdriver
import time

class Css_Selector_Eg_1:

    def Verify(self):

        driver = webdriver.Chrome()
        driver.get("https://demo.actitime.com/")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[contains(text(),'Male')]").is_selected())


selenium = Css_Selector_Eg_1()
selenium.Verify()