from selenium import webdriver
from helpers.driver import GetDriver
from helpers.elements import GetElement


class App:

    def __init__(self, driver):
        # initialize the driver
        self.driver_init = GetDriver(driver)
        # returns the driver
        self.driver = self.driver_init.get_driver()

    def get_page(self, url):
        return self.driver.get(url)

    def get_element(self, locatorType, element):
        """Gets element by its locator
        id, css_selector, partial_link_text, link_text, class_name, tag_name, xpath
        """

        elem = GetElement.by(self, driver=self.driver, locator=locatorType, element=element)

        if elem is None:
            return None
        else:
            return elem

app = App('chrome')
app.get_page('http://letskodeit.teachable.com/pages/practice')

print(app.get_element('id','alertbtn'))