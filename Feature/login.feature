#!/usr/bin/env python
# -*- coding: utf-8 -*-
Feature Login
  As A user I want to login

  Background:
    Given Access Tiki website
    And Choose Login / Register

  Scenario Outline: Login unsuccessful with incorrect phone number and/or password
    When Input invalid <phone_number>
#    And Input <password>
#    And Choose button Login
    Then Show error <message> correct
    Examples:
    |phone_number|message|
    |098645454|Số điện thoại không đúng định dạng.|