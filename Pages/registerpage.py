class RegisterPage:
    input_name_locator = '//input[@id="name"]'
    input_email_locator = '//input[@id="email"]'
    input_password_locator = '//input[@id="password"]'
    input_confirm_password_locator = '//input[@id="password_confirmation"]'
    button_signup_locator = '//input[@id="submit_button"]'

    def __init__(self, browser):
        self.browser = browser

    def input_name(self, text):
        element = self.browser.find_element_by_xpath(self.input_name_locator)
        self.browser.set_text_element(element, text, 2)
        return True

    def input_email(self, text):
        element = self.browser.find_element_by_xpath(self.input_email_locator)
        self.browser.set_text_element(element, text, 2)
        return True

    def input_password(self, text):
        element = self.browser.find_element_by_xpath(self.input_password_locator)
        self.browser.set_text_element(element, text, 2)
        return True

    def input_password_confirm(self, text):
        element = self.browser.find_element_by_xpath(self.input_password_confirm)
        self.browser.set_text_element(element, text, 2)
        return True

    def choose_btn_signup(self):
        element = self.browser.find_element_by_xpath(self.button_signup_locator)
        self.browser.click_element(element, 1)
        return True
