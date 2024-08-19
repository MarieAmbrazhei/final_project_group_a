import allure
import pytest
from test_project.pages.add_user_page import AddUserPageHelper
from test_project.pages.common_el_page import CommonElementsHelper
from test_project.pages.contact_add_page import AddContactHelper
from test_project.pages.contact_list_page import ContactListHelper
from test_project.urls.project_urls import PageUrls
from test_project.utils.constants.site_headers_names import Headers

""" Author: Marie Ambrazhei """
TEST_ID = "36820801"


@allure.id(TEST_ID)
@allure.parent_suite('UI Tests')
@allure.suite('Contact Table')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36820801",
                 name="Add Contact With Missing Required Fields")
@allure.title("[Contact list |36820801] Add Contact With Missing Required Fields")
@pytest.mark.ui
@pytest.mark.fast_ui
@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_add_contact_with_missing_required_fields(browsers_chrome, base_ui_url):
    browser = browsers_chrome[0]

    # CREATE HELPERS INSTANCES
    common_elements_helper = CommonElementsHelper(browser)
    add_user_page_helper = AddUserPageHelper(browser)
    contact_list_helper = ContactListHelper(browser)
    add_contact_helper = AddContactHelper(browser)

    with allure.step('Go to adding user page'):
        add_user_page_helper.get_url(base_ui_url + PageUrls.PAGE_ADD_USER_URL)

    with allure.step("Create Main User"):
        add_user_page_helper.register_main_user()

    with allure.step(f'Check header {Headers.CONTACT_LIST}'):
        common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    with allure.step('Click on button "Add new contact"'):
        contact_list_helper.get_btn_add_new_contact().click()

    with allure.step(f'Check header {Headers.ADD_CONTACT}'):
        common_elements_helper.get_page_title(Headers.ADD_CONTACT)

    with allure.step('Fill all inputs for new contact with invalid data'):
        add_contact_helper.fill_contact_with_invalid_data()
        common_elements_helper.get_btn_submit().click()

    with (allure.step('Check if error messages are displayed')):
        actual_error_msg = add_contact_helper.get_error_message().text
        expected_error_msg = (
            "Contact validation failed: firstName: Path `firstName` is required., "
            "lastName: Path `lastName` is required.")

        assert actual_error_msg == expected_error_msg, (f"Actual: {actual_error_msg}\nExpected:"
                                                        f" {expected_error_msg}\n")
