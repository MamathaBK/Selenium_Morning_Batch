from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.gmail.com")
time.sleep(5)
