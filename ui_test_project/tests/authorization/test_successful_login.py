"""Verifying successful registration."""
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# # """ Author: Valeria Kudelko """
TEST_ID = "36836333"


@allure.id(TEST_ID)
@allure.suite('Authorization')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36836333",
                 name="Successful login")
@pytest.mark.parametrize("browser", ["chrome"], indirect=True)
def test_successful_login(browser):
    """Checking successful login"""
    url = "https://thinking-tester-contact-list.herokuapp.com"
    browser.get(url)

    with allure.step('Enter valid email'):
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//input[@id="email"]')))
        email_input.send_keys('valid_email')

    with allure.step('Enter valid password'):
        password_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//input[@id="password"]')))
        password_input.send_keys('valid_password')

    with allure.step('Click sign up button'):
        sign_up_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@id="signup"]')))
        sign_up_button.click()

    with allure.step('Check main page is opened'):
        assert browser.current_url == (
            "https://thinking-tester-contact-list.herokuapp.com" "/contactList"
        )
