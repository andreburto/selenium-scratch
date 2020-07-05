# Standard library
from time import sleep

# Third-party
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


sleep(5)

driver = webdriver.Remote(command_executor='http://selenium-chrome:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
