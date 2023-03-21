#!/usr/bin/env python
# -*- coding: utf-8 -*-
class LoginPage:

    input_email_locator = ""
    input_password_locator = ""
    button_login_locator = ""
    error_email_locator = ""

    def __init__(self, driver):
        self.driver = driver

    def input_email(self, text):
        element = self.driver.find_element(self.input_email_locator)
        self.driver.set_text_element(element, text, 2)
        return True

    def input_password(self, text):
        element = self.driver.find_element(self.input_password_locator)
        self.driver.set_text_element(element, text, 2)
        return True

    def choose_btn_login(self):
        element = self.driver.find_element(self.button_login_locator)
        self.driver.click_element(element, 2)
        return True

    def get_error_message_email(self):
        element = self.driver.find_element(self.error_email_locator)
        message = self.driver.get_text_element(element)
        return message
