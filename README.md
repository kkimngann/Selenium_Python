# Python Selenium
````
This is the repo for automation tesing web https://ai.syllaby.io/, including the login and registration feature
Automation solution is implemeted by Python integrated the pytest-bdd and allure report
Supported browser: Chrome, Firefox
Steps to install and run test
  Setup Python 3.10 and environment variable
  Open command line in folder root source code folder
  Setup Python packages: command "pip3 install -r requirements.txt"
  1 - Update browser name at auto_test.cfg
  2 - Run test:
  Command to run all test: pytest --alluredir=allure-results tests
  Comment to run specific test: pytest --alluredir=allure-results tests/steps_defs/<testfile>.py
  3 - Wait for done
  ![image](https://user-images.githubusercontent.com/63134007/228115153-c23be3d6-33b5-41ae-83dd-584097d6bec8.png)
  4 - Command to generate report: allure generate --clean
  5 - To view the report please open file allure-report>>index.html
  The report will be show the summary and detail steps run
  ![image](https://user-images.githubusercontent.com/63134007/228115060-de1eb6fa-ea46-441a-9997-09cb13473311.png)

````
