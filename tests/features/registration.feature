#!/usr/bin/env python
# -*- coding: utf-8 -*-
Feature Registration
  As A user I want to registration new account

  Background:
    Given User access the website
    And User select button Login
    And User select Sign up
  Scenario Outline: Verify that user able to registration with valid data
    When User input name <name>
    And User input email <email>
    And User input password <password>
    And User input confirm password <confirm_password>
    And User select submit Sign up
    And User click on the user avatar
    Then Show current user email login is correct

    Examples:
      | name | email | password  | confirm_password |
      | Ngan | auto  | 123456789 | 123456789        |

  Scenario Outline: Verify that user not able to registration with invalid <name>, <email>, <password>, <confirm_password>
  When User input name <name>
  And User input email <email>
  And User input password <password>
  And User input confirm password <confirm_password>
  And User select submit Sign up
  Then Show correct error password message <password_message>
  Examples:
    | name | email                  | password  | confirm_password | password_message                          |
    | Ngan | ngan.nguyen@gmail.com  | 12345678  | 123456789        | The password confirmation does not match. |
    | Ngan | kkimngann1@yopmail.com | 123456789 | 123456789        | The email has already been taken.         |





