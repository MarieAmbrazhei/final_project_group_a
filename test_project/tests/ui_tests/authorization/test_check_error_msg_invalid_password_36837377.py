import allure
import pytest

from test_project.pages.add_user_page import AddUserPageHelper
from test_project.pages.common_el_page import CommonElementsHelper
from test_project.pages.login_page import LoginPageHelper
from test_project.urls.project_urls import PageUrls
from test_project.utils.rand_methods import Randoms

""" Author: Yury Buzinau """
TEST_ID = "36837377"


@allure.id(TEST_ID)
@allure.parent_suite('UI Tests')
@allure.suite('Authorization')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36837377",
                 name="Check error message. Invalid Password.")
@allure.title("[Authorization | 36837377] Check error message. Invalid Password.")
@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_check_error_msg_invalid_password_36837377(browsers_chrome):
    browser = browsers_chrome[0]

    # CREATE HELPERS INSTANCES
    common_elements_helper = CommonElementsHelper(browser)
    add_user_page_helper = AddUserPageHelper(browser)
    login_page_helper = LoginPageHelper(browser)

    with allure.step('Go to login page'):
        add_user_page_helper.get_url(PageUrls.PAGE_LOGIN_URL)

    with allure.step('Enter valid email'):
        login_page_helper.get_input_email().send_keys(Randoms.email())

    with allure.step('Enter invalid password'):
        login_page_helper.get_input_pass().send_keys(Randoms.int_gen(10))

    with allure.step('Click sign up button'):
        common_elements_helper.get_btn_submit().click()

    with allure.step(f'Check error message: "{login_page_helper.ERROR_MESSAGE}" is displayed'):
        expected_error_msg = login_page_helper.ERROR_MESSAGE
        actual_error_msg = login_page_helper.get_error_msg().text

        assert expected_error_msg == actual_error_msg, \
            (f"\nExpected error text: {expected_error_msg}"
             f"\nActual error text: {actual_error_msg}")
