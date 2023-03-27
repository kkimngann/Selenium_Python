import pytest

from browser.browser import Browser
import configparser

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')


@pytest.fixture(autouse=True, scope="session")
def browser():
    return Browser(BROWSER_NAME)


def pytest_bdd_before_scenario(request):
    print("this is before scenario")
    request.getfixturevalue("browser").get(URL)


def pytest_bdd_after_scenario(request):
    print("this is after scenario")
    request.getfixturevalue("browser").quit()

