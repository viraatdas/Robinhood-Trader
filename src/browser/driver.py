import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import EMAIL, PASSWORD


class Browser:
    def __init__(self):
        driver_path = os.getcwd() + "/src/browser/webdriver/geckodriver"

        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.driver.implicitly_wait(5)

    def login(self):
        self.driver.get("https://robinhood.com/login")
        inputElement = self.driver.find_element_by_xpath(
            "//input[@name='username']")
        inputElement.send_keys(EMAIL)

        inputElement = driver.find_element_by_xpath(
            "//input[@type='password']")
        inputElement.send_keys(PASSWORD)
