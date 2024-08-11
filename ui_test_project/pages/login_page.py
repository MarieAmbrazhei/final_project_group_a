from selenium.webdriver.common.by import By

from ui_test_project.pages._base_page import BasePage


class LoginPageLocators:
    LOCATOR_INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    LOCATOR_INPUT_PASS = (By.XPATH, '//input[@id="password"]')
    LOCATOR_BTN_SIGN_UP = (By.XPATH, '//button[@id="signup"]')
    LOCATOR_ERROR_MSG = (By.XPATH, '//span[@id="error"]')


class LoginPageHelper(BasePage):

    ERROR_MESSAGE = "Incorrect username or password"

    def get_input_email(self):
        return self.find_element_visible(LoginPageLocators.LOCATOR_INPUT_EMAIL)

    def get_input_pass(self):
        return self.find_element_visible(LoginPageLocators.LOCATOR_INPUT_PASS)

    def get_btn_sign_up(self):
        return self.find_element_visible(LoginPageLocators.LOCATOR_BTN_SIGN_UP)

    def get_error_msg(self):
        return self.find_element_visible(LoginPageLocators.LOCATOR_ERROR_MSG)
