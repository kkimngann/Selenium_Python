#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomePage:
    btn_login_locator = '//a[contains(@href, "login")]'

    def __init__(self, browser):
        self.browser = browser

    def choose_btn_login(self):
        element = self.browser.find_element_by_xpath(self.btn_login_locator)
        self.browser.click_element(element, 2)
        return True
