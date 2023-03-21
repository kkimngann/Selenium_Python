#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pytest
import os
import configparser

from pytest_bdd import scenarios, given
from Pages.homepage import HomePage
from test_basepage import test_basepage

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')

class test_login(test_basepage):
    def __init__(self):
        super().__init__()
        print("Hàm khởi tạo lớp con")


test_login_page = test_login()

@scenarios("../Feature/login.feature")
@given("User select button Login2")
def user_select_btn_login():
    homepage = HomePage(test_login_page.driver)
    homepage.choose_btn_login()
    return True


@given("User access the website2")
def step_impl():
    test_login_page.driver.get(URL)
    raise NotImplementedError(u'STEP: Given User access the website')