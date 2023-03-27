class RegisterPage:
    input_name_locator = '//input[@id="name"]'
    input_email_locator = '//input[@id="email"]'
    input_password_locator = '//input[@id="password"]'
    input_confirm_password_locator = '//input[@id="password_confirmation"]'
    button_signup_locator = '//button[@id="submit_button"]'
    error_password_locator = input_password_locator + '/following-sibling::div/strong'
    header_message_locator = '//div[@id="kt_docs_toast_toggle"]'
    header_title_locator = '//strong'
    header_body_locator = '//div[contains(@class, "toast-body")]'


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
        element = self.browser.find_element_by_xpath(self.input_confirm_password_locator)
        self.browser.set_text_element(element, text, 2)
        return True

    def choose_btn_signup(self):
        element = self.browser.find_element_by_xpath(self.button_signup_locator)
        self.browser.click_element(element, 1)
        return True

    def get_error_message_password(self):
        element = self.browser.find_element_by_xpath(self.error_password_locator)
        message = self.browser.get_text_element(element)
        return message

    def check_login_successful(self):
        toast = self.browser.find_element_by_xpath(self.header_message_locator)
        toast_header = self.browser.find_child_element_by_xpath(toast, self.header_title_locator)
        toast_body = self.browser.find_child_element_by_xpath(toast, self.header_body_locator)
        assert self.browser.get_text_element(toast_header) == "MESSAGE" and self.browser.get_text_element(toast_body) == "Logout Successful"


