#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.locator import Locator
class LoginPage():
    def __init__(self,browser):
        self.browser = browser

    def input_phone_number(self, text):
        element = self.browser.find_element(Locator.txt_phone)
        self.browser.set_text_element(element, text,2)
        return True

    def input_password(self,text):
        element = self.browser.find_element(Locator.txt_pass)
        self.browser.set_text_element(element, text,2)
        return True

    def choose_btn_login(self):
        element = self.browser.find_element(Locator.btn_login)
        self.browser.click_element(element,2)
        return True

    def get_error_message(self):
        element = self.browser.find_element(Locator.message_error)
        message = self.browser.get_text_element(element)
        return message
