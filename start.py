from helpers.driver import GetDriver
from helpers.elements import GetElement, Element


class App:

    def __init__(self, driver):
        # initialize the driver
        self.driver_init = GetDriver(driver)
        # returns the driver
        self.driver = self.driver_init.get_driver()
        self.element = None

    def get_page(self, url):
        return self.driver.get(url)

    def get_element(self, locator_type, element):
        """Gets element by its locator
        id, css_selector, partial_link_text, link_text, class_name, tag_name, xpath
        """

        e = Element(self.driver, locator_type, element)

        self.element = e


app = App('chrome')
app.get_page('http://letskodeit.teachable.com/pages/practice')
app.get_element('xpath','//input[@id="alertbtn"]')
print(app.element.get_attribute('id'))
print(app.element.get_next_element(element_type='input').get_attribute('id'))


# app -> create driver
# app.get_page -> url
# app.get_element ->
