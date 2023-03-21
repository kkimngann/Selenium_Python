from selenium import webdriver

# specify the path to the chromedriver executable
chromedriver_path = '/Users/nganntk/Documents/NGANNTK/Python_Selenium/DriverMacOS/chromedriver'

# create a new Chrome browser instance
browser = webdriver.Chrome(executable_path=chromedriver_path)

# navigate to Google.com
browser.get('https://www.google.com')

# quit the browser
browser.quit()