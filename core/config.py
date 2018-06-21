from selenium import webdriver


# Driver path
driver_path = '/usr/lib/chromium-browser/chromedriver'

# Experimental options to prevent browser from closing after use
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)