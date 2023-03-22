Feature Login
  As A user I want to login
  Background:
    Given User access the website
    And User select button Login

  Scenario Outline: Verify that user not able to login with incorrect <email>, <password>
    When User input email <email>
    And User input password <password>
    And User select Login
    Then Show correct error email message <message_email>
    And Show correct error password message <message_password>
    Examples:
      | email                   | password    | message_email                            | message_password |
      | ngan.nguyen13           | 12323213123 | The email must be a valid email address. |                  |
      | ngan.nguyen13@gmail.com | 12323213123 | The selected email is invalid.           |                  |
      | ngan.nguyen13@gmail.com | 12323       |                                          | The password must be at least 8 characters.                 |

