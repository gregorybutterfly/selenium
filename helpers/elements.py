from selenium.webdriver.common.by import By


class Element:

    def __init__(self, driver, locator_type, element_to_find):
        self.driver = driver
        self.locator_type = locator_type
        self.element_to_find = element_to_find
        self.element = self.get_element()
        self.next_element = None

    def get_element(self):

        c = GetElement(self.driver)

        return c.by(locator=self.locator_type, element=self.element_to_find)

    def get_attribute(self, attr):
        return self.element.get_attribute(attr)

    def get_next_element(self, element_type):
        if self.locator_type == 'xpath':

            element_to_find = self.element_to_find + '//following-sibling::' + element_type

            c = GetElement(self.driver)
            return c.by(locator=self.locator_type, element=element_to_find)

class GetElement:
    """Get element from given url
    """

    def __init__(self, driver):
        self.driver = driver

    def by(self, locator, element):
        """Returns element by ID
        """

        if locator.lower() == 'id':
            return self.driver.find_element(By.ID, element)
        elif locator.lower() == 'css_selector':
            return self.driver.find_element(By.CSS_SELECTOR, element)
        elif locator.lower() == 'partial_link_text':
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, element)
        elif locator.lower() == 'link_text':
            return self.driver.find_element(By.LINK_TEXT, element)
        elif locator.lower() == 'class_name':
            return self.driver.find_element(By.CLASS_NAME, element)
        elif locator.lower() == 'tag_name':
            return self.driver.find_element(By.TAG_NAME, element)
        elif locator.lower() == 'name':
            return self.driver.find_element(By.NAME, element)
        elif locator.lower() == 'xpath':
            return self.driver.find_element(By.XPATH, element)
        else:
            return None