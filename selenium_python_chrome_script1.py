import unittest
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class TestRequests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("about:blank")
        self.driver.implicitly_wait(10.0)
        self.driver.maximize_window()

    def save_screenshot(self):
        name = "Taurus_screenshot"
        self.driver.get_screenshot_as_file(name + ".png")

    def test_method(self):
        # start request: http://www.blazedemo.com/
        self.driver.get('http://www.blazedemo.com/')
        sleep(1.5)
        find_flights_button = "//input[@value='Find Flights']"
        self.driver.find_element(By.XPATH, find_flights_button).click()
        sleep(2.5)
        self.save_screenshot()
        # end request: http://www.blazedemo.com/

    def tearDown(self):
        self.driver.quit()

