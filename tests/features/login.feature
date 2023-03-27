Feature Login
  As A user I want to login
  Background:
    Given User access the website
    And User select button Login

  Scenario Outline: : Verify that user not able to login with incorrect <email>, <password>
    When User input email <email>
    And User input password <password>
    And User select Login
    Then Show correct error email message <email_message>
    And Show correct error password message <password_message>
    Examples:
      | email                   | password | email_message                            | password_message                            |
      | ngan.nguyen13@gmail.com | 123      | The selected email is invalid.           | The password must be at least 8 characters. |
      | ngan.nguyen13           | 12345678 | The email must be a valid email address. | None                                        |
      | ngan.nguyen13@gmail.com | 12345678 | The selected email is invalid.           | None                                        |




