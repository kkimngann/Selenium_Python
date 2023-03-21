#!/usr/bin/env python
# -*- coding: utf-8 -*-
Feature Registration
  As A user I want to registration new account

  Background:
    Given User access the website
    And User select button Login
    And User select Sign up

  Scenario Outline: Verify that user not able to registration with invalid <name>, <email>, <password>, <confirm_password>
    When User input name <name>
    And User input email <email>
    And User input password <password>
    And User input confirm password <confirm_password>
    And User select Sign up
    Examples:
      | name | email                 | password | confirm_password |
      |      | ngan.nguyen@gmail.com |          |                  |