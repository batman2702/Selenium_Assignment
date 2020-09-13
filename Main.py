from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Assessment():
    def test(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Downloads\\chromedriver.exe")
        driver.get("http://jt-dev.azurewebsites.net/#/SignUp")
        time.sleep(5)
        driver.find_element_by_id("name").send_keys("vybhav")
        driver.find_element_by_id("orgName").send_keys("vybhav")
        driver.find_element_by_id("singUpEmail").send_keys("aazxc48@gmail.com")
        driver.find_element_by_css_selector(".ui-checkbox>.black-color.ng-binding").click()
        driver.find_element_by_css_selector(".btn.btn-block.btn-custom.ng-binding").click()
        driver.close()

selenium_object=Assessment()
selenium_object.test()
        
