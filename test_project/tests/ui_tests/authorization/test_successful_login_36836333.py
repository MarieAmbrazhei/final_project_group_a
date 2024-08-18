import allure
import pytest

from test_project.utils.constants.site_headers_names import Headers
from test_project.pages.add_user_page import AddUserPageHelper
from test_project.pages.common_el_page import CommonElementsHelper
from test_project.pages.login_page import LoginPageHelper
from test_project.urls.project_urls import PageUrls
from test_project.utils.rand_methods import Randoms

""" Author: Yury Buzinau """
TEST_ID = "36836333"


@allure.id(TEST_ID)
@allure.parent_suite('UI Tests')
@allure.suite('Authorization')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36836333",
                 name="Successful Login")
@allure.title("[Authorization | 36836333]  Successful Login")
@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_successful_login_36836333(browsers_chrome, base_ui_url):
    browser = browsers_chrome[0]

    # CREATE HELPERS INSTANCES
    common_elements_helper = CommonElementsHelper(browser)
    add_user_page_helper = AddUserPageHelper(browser)
    login_page_helper = LoginPageHelper(browser)

    # CREATE TEST VARIABLES
    main_user_email = Randoms.email()
    main_user_pass = Randoms.int_gen(10)

    with allure.step('Go to adding user page'):
        add_user_page_helper.get_url(base_ui_url + PageUrls.PAGE_ADD_USER_URL)

    with allure.step('Create Main User'):
        add_user_page_helper.register_main_user(
            email=main_user_email,
            password=main_user_pass
        )

    with allure.step(f'Check header {Headers.CONTACT_LIST}'):
        common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    with allure.step("Logout from admin panel"):
        common_elements_helper.get_btn_logout().click()

    with allure.step(f'Check header {Headers.CONTACT_LIST_APP}'):
        common_elements_helper.get_page_title(Headers.CONTACT_LIST_APP)

    with allure.step('Enter valid email'):
        login_page_helper.get_input_email().send_keys(main_user_email)

    with allure.step('Enter valid password'):
        login_page_helper.get_input_pass().send_keys(main_user_pass)

    with allure.step('Click sign up button'):
        common_elements_helper.get_btn_submit().click()

    with allure.step(f'Check header {Headers.CONTACT_LIST}'):
        common_elements_helper.get_page_title(Headers.CONTACT_LIST)
