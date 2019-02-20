from selenium import webdriver
import time

class Get_Image_Tags:

    def img_tag(self):

        driver = webdriver.Chrome()
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()
        element = driver.find_elements_by_xpath("//img")
        print(type(element))
        print(element)


for ele in element:
    url = ele.get_attribute("img")
    print(url)


selenium = Get_Image_Tags()
selenium.img_tag()