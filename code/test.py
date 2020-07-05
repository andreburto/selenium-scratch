# Standard library
from time import sleep

# Third-party
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

REMOTE_CMD_EXE = "http://selenium-chrome:4444/wd/hub"


while True:
    try:
        requests.get(REMOTE_CMD_EXE)
        break
    except:
        pass

driver = webdriver.Remote(command_executor=REMOTE_CMD_EXE, desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
