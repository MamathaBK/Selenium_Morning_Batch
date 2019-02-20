from selenium import webdriver
import time

class VerficationMethods:

    def Verify(self):

        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        print(driver.find_element_by_xpath("//*[contains(text(),'Male')]").is_selected())
        # print(driver.find_elements_by_class_name("_58mt").__getattribute__()
        # print(driver.find_element_by_id("u_0_a").is_selected()

        # print(driver.find_element_by_xpath("//*[@id="u_0_a"]").is_selected())
        # driver.find_element_by_xpath("//*[@id="u_0_a"]").click()
        # time.sleep(5)
        # print(driver.find_element_by_xpath("//*[@id="u_0_a"]")).is_selected())

selenium = VerficationMethods()
selenium.Verify()
