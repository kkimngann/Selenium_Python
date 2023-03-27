#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

config = configparser.ConfigParser()
config.read('auto_test.cfg')


class Browser:
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.driver = self.open_browser()

    def open_browser(self):
        os_name = config.get("OS", "os_name")
        config_menu_name = "BROWSER PATH " + os_name
        if self.browser_name == 'chrome':
            chromedriver_path = config.get(config_menu_name, "chrome_path")
            opt = webdriver.ChromeOptions()
            opt.add_argument("--remote-allow-origins=*")
            driver = webdriver.Chrome(executable_path=chromedriver_path, options=opt)
            driver.implicitly_wait(5)
            driver.maximize_window()
            return driver
        elif self.browser_name == 'firefox':
            browser_path = config.get(config_menu_name, "firefox_path")
            driver = webdriver.Firefox(executable_path=browser_path)
            driver.implicitly_wait(5)
            driver.maximize_window()
            return driver

        """
        elif self.browser_name == 'edge':
            driver = webdriver.Edge()
            return driver
        elif self.browser_name == 'safari':
            driver = webdriver.Safari()
            driver.implicitly_wait(5)
            driver.maximize_window()
            return driver
        """

    def find_element_by_xpath(self, xpath_locator):
        try:
            element = self.driver.find_element(By.XPATH, xpath_locator)
            return element
        except:
            return False

    def find_child_element_by_xpath(self,element,xpath_locator):
        try:
            child_element = element.find_element(By.XPATH, xpath_locator)
            return child_element
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
            return element.text.strip()
        except:
            return ''

    def get(self, url):
        self.driver.get(url)

    def quit(self):
        if self.driver is not None:
            self.driver.quit()
