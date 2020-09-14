from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Assessment():
    def test(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Downloads\\chromedriver.exe")
        driver.get("http://jt-dev.azurewebsites.net/#/SignUp")
        time.sleep(5)
        river.find_element_by_css_selector('div#language .pull-left.ui-select-match-text').click()
        val=driver.find_elements_by_xpath("//ul[@class='ui-select-choices ui-select-choices-content ui-select-dropdown dropdown-menu ng-scope']/li[@class='ui-select-choices-group']/div/a/div[@class='ng-binding ng-scope']")
        ls=set()
        for temp in val:
            ls.add(temp.text)
        if ls and list_of_languages:
            print("Both Languages are present")
        driver.find_elements_by_xpath("//ul[@class='ui-select-choices ui-select-choices-content ui-select-dropdown dropdown-menu ng-scope']/li[@class='ui-select-choices-group']/div/a/div[@class='ng-binding ng-scope']")[0].click()
        driver.find_element_by_id("name").send_keys("vybhav")
        driver.find_element_by_id("orgName").send_keys("vybhav")
        driver.find_element_by_id("singUpEmail").send_keys("sreshtavybhav@gmail.com@gmail.com")
        driver.find_element_by_css_selector(".ui-checkbox>.black-color.ng-binding").click()
        driver.find_element_by_css_selector(".btn.btn-block.btn-custom.ng-binding").click()
        driver.close()

selenium_object=Assessment()
selenium_object.test()
        
