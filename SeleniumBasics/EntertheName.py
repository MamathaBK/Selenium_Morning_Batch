from selenium import webdriver
import time

class Enter_Name:

    def Send_Text(self):
        driver = webdriver.Chrome()
        driver.get("file:///C:/Users/Mamatha/Desktop/Practice.html")
        driver.maximize_window()
        driver.find_element_by_id('name').send_keys("Mamatha")
        time.sleep(5)

Name = Enter_Name()
Name.Send_Text()
