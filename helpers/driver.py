from selenium import webdriver
from scraper.core.config import driver_path, opts


class GetDriver:
    """ Create new driver for Selenium and use additional options if necessary.

    maximize_window: enlarges browser window
    waiting_time: set number of seconds for a browser to wait until it tries to perform same action again.
    """

    def __init__(self, driver):

        if driver.lower() is 'chrome':
            self.driver = webdriver.Chrome(executable_path=driver_path, options=opts)
        else:
            print('Driver ' + driver + ' not found!')

    def maximize_window(self):
        """Maximizes browser window
        """
        return self.driver.maximize_window()

    def waiting_time(self, secs):
        """Set waiting time.
        If element not found, wait given number if seconds and try again.
        """
        return self.driver.implicitly_wait()

