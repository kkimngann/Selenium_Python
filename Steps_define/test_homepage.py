#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

from Steps_define.test_basepage import TestBasePage

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Pages.homepage import HomePage
from pytest_bdd import scenarios
import configparser

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')
# Scenarios
@scenarios('../login.feature')


class TestHomePage(TestBasePage):
    homepage = HomePage

    def __init__(self):
        TestBasePage.__init__(self)


