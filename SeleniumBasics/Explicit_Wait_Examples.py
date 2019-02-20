from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWait:

    def send_text(self):
            base_url = "file:///C:/Users/Mamatha/Desktop/Practice.html"
            driver = webdriver.Chrome()
            driver.get(base_url)
            driver.maximize_window()
            driver.implicitly_wait(3)
            ele = WebDriverWait(driver,10)
            ele.until(EC.presence_of_element_located((By.ID,"Pythonradio")))
            print("Wait executed")
            print(driver.find_element_by_id("Pythonradio").is_selected())
            print(ele)
            driver.implicitly_wait(3)

ExplicitWait().send_text()




