from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://pypi.org/")
time.sleep(5)

expected_value = 'Log in'
text_value = driver.find_element_by_xpath("//a[contains(text(),'Log in')]").text
if expected_value == text_value:
    print("test case passed")
else:
    print("test case failed")