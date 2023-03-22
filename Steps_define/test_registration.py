from pytest_bdd import scenario, given, when, then, parsers, scenarios

from Pages.homepage import HomePage
from Pages.loginpage import LoginPage
from Pages.registerpage import RegisterPage
from Steps_define.test_basepage import test_basepage
import configparser

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')

scenarios('../Feature/registration.feature')
class test_registration(test_basepage):
    def __init__(self):
        super().__init__()


test_page = test_registration()
home_page = HomePage(test_page.browser)
login_page = LoginPage(test_page.browser)
register_page = RegisterPage(test_page.browser)

@given('User access the website')
def function_given():
    print("Access the website")
    home_page.browser.get(URL)


@given('User select button Login')
def select_login():
    print("User select button Login")
    home_page.choose_btn_login()

@given("User select Sign up")
def step_impl():
    login_page.choose_btn_sign_up()


@then(parsers.parse("User input name {name}"))
def step_impl(name):
    register_page.input_name(name)
