"""Checking authorization with an incorrect user name"""
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# """ Author: Valeria Kudelko """
TEST_ID = "36837160"


@allure.id(TEST_ID)
@allure.suite('Authorization')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36837160",
                 name="Invalid user name")
@pytest.mark.parametrize("browser", ["chrome"], indirect=True)
def test_login_with_invalid_email(browser):
    """Checking login with invalid email"""
    url = "https://thinking-tester-contact-list.herokuapp.com"
    browser.get(url)

    with allure.step('Enter invalid email'):
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//input[@id="email"]')))
        email_input.send_keys('invalid_email')

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

    with allure.step('Check error message is displayed'):
        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@class="error-message"]')))
        assert error_message.text == "Invalid email or password"
