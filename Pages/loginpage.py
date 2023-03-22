#!/usr/bin/env python
# -*- coding: utf-8 -*-
class LoginPage:

    input_email_locator = '//input[@id="email"]'
    input_password_locator = '//input[@id="password"]'
    button_login_locator = '//button[@id="submit_button"]'
    error_email_locator = input_email_locator + '/following-sibling::div/strong'
    error_password_locator = input_password_locator + '/following-sibling::div/strong'
    button_sign_up_locator = '//a[contains(@href, "register")]'

    def __init__(self, browser):
        self.browser = browser

    def input_email(self, text):
        element = self.browser.find_element_by_xpath(self.input_email_locator)
        self.browser.set_text_element(element, text, 2)
        return True

    def input_password(self, text):
        element = self.browser.find_element_by_xpath(self.input_password_locator)
        self.browser.set_text_element(element, text, 2)
        return True

    def choose_btn_login(self):
        element = self.browser.find_element_by_xpath(self.button_login_locator)
        self.browser.click_element(element, 1)
        return True

    def get_error_message_email(self):
        element = self.browser.find_element_by_xpath(self.error_email_locator)
        message = self.browser.get_text_element(element)
        return message

    def get_error_message_password(self):
        element = self.browser.find_element_by_xpath(self.error_password_locator)
        message = self.browser.get_text_element(element)
        return message

    def choose_btn_sign_up(self):
        element = self.browser.find_element_by_xpath(self.button_sign_up_locator)
        self.browser.click_element(element, 1)
