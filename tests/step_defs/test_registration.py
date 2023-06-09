import time

from pytest_bdd import scenarios, given, when, parsers, then
from pytest_bdd.parsers import parse

from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.registerpage import RegisterPage
import configparser

from tests.step_defs.base_steps import base_steps

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')

# scenarios
scenarios('../features/registration.feature')


class test_registration(base_steps):
    def __init__(self):
        super().__init__()

    def tearDown(self):
        super().teardown()


test_page = test_registration()
home_page = HomePage(test_page.browser)
login_page = LoginPage(test_page.browser)
register_page = RegisterPage(test_page.browser)


@given('User access the website')
def function_given():
    print('Access the website')
    home_page.browser.get(URL)


@given('User select button Login')
def select_login():
    print('User select button Login')
    home_page.choose_btn_login()


@given('User select Sign up')
def step_impl():
    login_page.choose_btn_sign_up()


@when(parse('User input name {name}'))
def step_impl(name):
    print('User input name %s' % name)
    register_page.input_name(name)


@when(parse('User input email {email}'))
def step_impl(email):
    if email == "auto":
        email = "test" + str(time.time()) + "@yopmail.com"
    print('User input email %s' % email)
    register_page.input_email(email)


@when(parse('User input password {password}'))
def step_impl(password):
    print('User input password %s' % password)
    register_page.input_password(password)


@when(parse('User input confirm password {confirm_password}'))
def step_impl(confirm_password):
    print('User input confirm password %s' % confirm_password)
    register_page.input_password_confirm(confirm_password)


@when('User select submit Sign up')
def step_impl():
    print('User select submit Sign up')
    register_page.choose_btn_signup()


@then(parse('Show correct error password message {password_message}'))
def step_impl(password_message):
    print('Show correct error password message %s' % password_message)
    if password_message != 'None':
        actual_message = register_page.get_error_message_password()
        assert actual_message == password_message


@then(parse('Show correct error email message {email_message}'))
def step_impl(email_message):
    print('Show correct error email message %s' % email_message)
    if email_message != 'None':
        actual_message = register_page.get_error_email_password()
        assert actual_message == email_message


@then("Show correct message register successful")
def step_impl():
    register_page.check_login_successful()


@when("User click on the user avatar")
def step_impl():
    home_page.click_user_avatar()


@then("Show current user email login is correct")
def step_impl():
    actual_email = home_page.get_current_email()
    assert "@yopmail" in actual_email
