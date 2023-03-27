#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from browser.browser import Browser
import configparser

config = configparser.ConfigParser()
config.read('auto_test.cfg')

URL = config.get('URL', 'url')
BROWSER_NAME = config.get('BROWSER', 'browser')


class base_steps:
    def __init__(self):
        self.browser = Browser(BROWSER_NAME)

    def setup(self):
        print('----------------------START TEST-------------------------')

    def teardown(self):
        print('------------------------END TEST-------------------------')
        self.browser.driver.quit()
