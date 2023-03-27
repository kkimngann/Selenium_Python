# -*- coding: utf-8 -*-
import sys
import os

from pytest_bdd.parsers import parse

from tests.step_defs.conftest import browser
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pytest_bdd import scenarios, given, when, then
import configparser

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

config = configparser.ConfigParser()
config.read('auto_test.cfg')

# Scenarios
scenarios('../features/login2.feature')


home_page = HomePage(browser)
login_page = LoginPage(browser)

@given('User select button Login 2')
def select_login(browser):
    print('User select button Login')
    home_page2 = HomePage(browser)
    home_page2.choose_btn_login()


@when(parse('User input email {email}'))
def step_impl(browser, email):
    print('User input email %s' % email)
    login_page2 = LoginPage(browser)
    login_page2.input_email(email)


@when(parse('User input password {password}'))
def step_impl(password):
    print('User input password %s' % password)
    login_page.input_password(password)


@when('User select Login')
def step_impl(browser):
    print('User select Login')
    login_page.choose_btn_login()


@then(parse('Show correct error email message {message_email}'))
def step_impl(message_email):
    print('Show correct error email message %s' % message_email)
    if message_email != 'None':
        actual_message = login_page.get_error_message_email()
        assert actual_message == message_email


@then(parse('Show correct error password message {password_message}'))
def step_impl(browser, password_message):
    print('Show correct error password message %s' % password_message)
    if password_message != 'None':
        actual_message = login_page.get_error_message_password()
        assert actual_message == password_message
