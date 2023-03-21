#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Browser.browser import Browser
from Pages.homepage import HomePage
from Pages.loginpage import LoginPage
from pytest_bdd import scenarios, given, when, then, parsers
import configparser

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER','browser')
# Scenarios
scenarios('../Feature/login.feature')

def setup():
    # print('----------------------START TEST-------------------------')
    global obj_browser
    obj_browser = Browser(BROWSER_NAME)

def teardown():
    # print('------------------------END TEST-------------------------')
    obj_browser.driver.quit()

@given('User select button Login')
def function_given():
    print("Access Tiki website")
    obj_browser.driver.get(URL)

@given('User access the website')
def choose_more():
    page = HomePage(obj_browser)
    page.choose_btn_login()