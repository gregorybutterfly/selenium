from selenium.webdriver.common.by import By


class GetElement:
    """Get element of a page
    """

    def by(self, driver, locator, element):
        """Returns element by ID
        """

        if locator.lower() == 'id':
            return driver.find_element(By.ID, element)
        elif locator.lower() == 'css_selector':
            return driver.find_element(By.CSS_SELECTOR, element)
        elif locator.lower() == 'partial_link_text':
            return driver.find_element(By.PARTIAL_LINK_TEXT, element)
        elif locator.lower() == 'link_text':
            return driver.find_element(By.LINK_TEXT, element)
        elif locator.lower() == 'class_name':
            return driver.find_element(By.CLASS_NAME, element)
        elif locator.lower() == 'tag_name':
            return driver.find_element(By.TAG_NAME, element)
        elif locator.lower() == 'name':
            return driver.find_element(By.NAME, element)
        elif locator.lower() == 'xpath':
            return  driver.find_element(By.XPATH, element)
        else:
            return None