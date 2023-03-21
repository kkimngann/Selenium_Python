#!/usr/bin/env python
# -*- coding: utf-8 -*-
class HomePage:
    btn_login_locator = "//a[contains(@href, \"login\")]"

    def __init__(self, driver):
        self.driver = driver

    def choose_btn_login(self):
        element = self.driver.find_element(self.btn_login_locator)
        self.driver.click_element(element, 2)
        return True
