#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import sys
import os

from Steps_define.test_basepage import test_basepage

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Browser.browser import Browser
from Pages.homepage import HomePage
from Pages.loginpage import LoginPage
from pytest_bdd import scenarios, given, when, then, parsers
import configparser

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')
# Scenarios
scenarios('../Feature/login.feature')


class test_login(test_basepage):
    def __init__(self):
        super().__init__()


test_page = test_login()
home_page = HomePage(test_page.browser)
login_page = LoginPage(test_page.browser)


@given('User access the website')
def function_given():
    print("Access the website")
    home_page.browser.get(URL)


@given('User select button Login')
def select_login():
    print("User select button Login")
    home_page.choose_btn_login()


@when(parsers.parse("User input email {email}"))
def step_impl(email):
    login_page.input_email(email)


@when(parsers.parse("User input password {password}"))
def step_impl(password):
    login_page.input_password(password)


@when("User select Login")
def step_impl():
    login_page.choose_btn_login()


@then(parsers.parse("Show correct error email message {message_email}"))
def step_impl(message_email):
    if message_email != "":
        actual_message = login_page.get_error_message_email()
        assert actual_message == message_email


@then(parsers.parse("Show correct error password message {message_password}"))
def step_impl(message_password):
    if message_password != "":
        actual_message = login_page.get_error_message_password()
        assert actual_message == message_password

