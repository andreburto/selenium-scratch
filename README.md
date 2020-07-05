# Docker-based Selenium Tests

### About

A proof-of-concept setup to run Seleniun tests in a Docker container. 
This means no need to manually install Chrome driver, and it can run in a pipeline.

### Usage

The needed commands to use this POC.

1. `docker-compose build` to build the needed image.
2. `docker-compose run selenium-test` to stand up the remote Selenium remote WebDriver and run the Python tests (in that order).

### Links

Relavent links used in setting this up.

 * [Selenium with Python](https://selenium-python.readthedocs.io/)
   * [2.1 Simple Usage](https://selenium-python.readthedocs.io/getting-started.html#simple-usage)
   * [2.5 Using Selenium with remote WebDriver](https://selenium-python.readthedocs.io/getting-started.html#using-selenium-with-remote-webdriver)
* [Selenium Grid Standalone - Chrome](https://github.com/SeleniumHQ/docker-selenium/tree/master/StandaloneChrome)
