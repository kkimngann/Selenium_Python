#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomePage:
    btn_login_locator = '//a[contains(@href, "login")]'
    current_user_ava_locator = '//div[@id="kt_header_user_menu_toggle"]'
    current_user_email_locator = '//div[@id="kt_header_user_menu_toggle"]//a'

    def __init__(self, browser):
        self.browser = browser

    def choose_btn_login(self):
        element = self.browser.find_element_by_xpath(self.btn_login_locator)
        self.browser.click_element(element, 2)
        return True

    def click_user_avatar(self):
        element = self.browser.find_element_by_xpath(self.current_user_ava_locator)
        self.browser.click_element(element, 2)
        return True

    def get_current_email(self):
        element = self.browser.find_element_by_xpath(self.current_user_email_locator)
        current_email = self.browser.get_text_element(element)
        return current_email
