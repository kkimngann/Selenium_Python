#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import time

from behave.formatter import null
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

config = configparser.ConfigParser()
config.read('auto_test.cfg')


class Browser:
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.driver = self.open_browser()

    def open_browser(self):
        global driver
        os_name = config.get("OS", "os_name")
        config_menu_name = "BROWSER PATH " + os_name
        if self.browser_name == 'ie':
            browser_path = config.get(config_menu_name, "ie_path")
            driver = webdriver.Ie(executable_path=browser_path)
            time.sleep(5)
        elif self.browser_name == 'chrome':
            chromedriver_path = config.get(config_menu_name, "chrome_path")
            driver = webdriver.Chrome(executable_path=chromedriver_path)
            driver.implicitly_wait(5)
            driver.maximize_window()
            driver.get('https://www.google.com')
            return driver
        elif self.browser_name == 'firefox':
            browser_path = config.get(config_menu_name, "firefox_path")
            driver = webdriver.Firefox(executable_path=browser_path)

        elif self.browser_name == 'edge':
            driver = webdriver.Edge()
        elif self.browser_name == 'safari':
            driver = webdriver.Safari()




    def find_element(self, xpath_element):
        try:
            element = self.driver.find_element(By.XPATH, xpath_element)
            return element
        except:
            return False

    def click_element(self, element, delay_time):
        try:
            element.click()
            time.sleep(delay_time)
        except:
            return False

    def set_text_element(self, element, text, delay_time):
        try:
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.DELETE)
            element.send_keys(text)
            time.sleep(delay_time)
        except:
            return False

    def get_text_element(self, element):
        try:
            return element.text
        except:
            return ''

    def get(self, url):
        self.driver.get(url)

    def quit(self):
        if self.driver is not None:
            self.driver.quit()
