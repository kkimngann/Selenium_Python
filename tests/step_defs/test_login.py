#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

from pytest_bdd.parsers import parse

from tests.step_defs.test_basepage import test_basepage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pytest_bdd import scenarios, given, when, then
import configparser

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')
# Scenarios
scenarios('../features/login.feature')


class test_login(test_basepage):
    def __init__(self):
        super().__init__()


test_page = test_login()
home_page = HomePage(test_page.browser)
login_page = LoginPage(test_page.browser)


@given('User access the website')
def function_given():
    print('Access the website')
    home_page.browser.get(URL)


@given('User select button Login')
def select_login():
    print('User select button Login')
    home_page.choose_btn_login()


@when(parse('User input email {email}'))
def step_impl(email):
    print('User input email %s' % email)
    login_page.input_email(email)


@when(parse('User input password {password}'))
def step_impl(password):
    print('User input password %s' % password)
    login_page.input_password(password)


@when('User select Login')
def step_impl():
    print('User select Login')
    login_page.choose_btn_login()


@then(parse('Show correct error email message {message_email}'))
def step_impl(message_email):
    print('Show correct error email message %s' % message_email)
    if message_email != 'None':
        actual_message = login_page.get_error_message_email()
        assert actual_message == message_email


@then(parse('Show correct error password message {password_message}'))
def step_impl(password_message):
    print('Show correct error password message %s' % password_message)
    if password_message != 'None':
        actual_message = login_page.get_error_message_password()
        assert actual_message == password_message
