import unittest
from selenium import webdriver

class FirstTest(unittest.TestCase)
    def test_first_selenium_test(self):
        self.driver = webdriver.Chrome("/Applications/chromedriver")
        self.driver.maximize_window()
        self.driver.get