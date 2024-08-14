from selenium.webdriver.common.by import By
from test_project.pages._base_page import BasePage
from test_project.pages.common_el_page import CommonElementsHelper
from test_project.utils.rand_methods import Randoms


class AddUserPageLocators:
    LOCATOR_INPUT_FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    LOCATOR_INPUT_LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    LOCATOR_INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    LOCATOR_INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')


class AddUserPageHelper(BasePage):

    def get_input_first_name(self):
        return self.find_element_visible(AddUserPageLocators.LOCATOR_INPUT_FIRST_NAME)

    def get_input_last_name(self):
        return self.find_element_visible(AddUserPageLocators.LOCATOR_INPUT_LAST_NAME)

    def get_input_email_name(self):
        return self.find_element_visible(AddUserPageLocators.LOCATOR_INPUT_EMAIL)

    def get_input_password_name(self):
        return self.find_element_visible(AddUserPageLocators.LOCATOR_INPUT_PASSWORD)

    """ METHODS """

    def register_main_user(
            self,
            *,
            email=None,
            password=None):

        self.get_input_first_name().send_keys(Randoms.rand_word(length=10))
        self.get_input_last_name().send_keys(Randoms.rand_word(length=10))

        if not email:
            self.get_input_email_name().send_keys(Randoms.email_gen(length=10))
        else:
            self.get_input_email_name().send_keys(email)

        if not password:
            self.get_input_password_name().send_keys(Randoms.int_gen(length=10))
        else:
            self.get_input_password_name().send_keys(password)

        CommonElementsHelper(self.driver).get_btn_submit().click()
