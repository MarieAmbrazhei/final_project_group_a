import allure
import pytest

from ui_test_project.pages.add_user_page import AddUserPageHelper
from ui_test_project.pages.common_el_page import CommonElementsHelper
from ui_test_project.pages.contact_add_page import AddContactHelper
from ui_test_project.pages.contact_list_page import ContactListHelper
from ui_test_project.urls.site_page_urls import PageUrls
from ui_test_project.utils.constants.site_headers_names import Headers


@allure.suite('Contacts')
@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_create_contact_with_invalid_data(browsers_chrome):
    browser = browsers_chrome[0]

    with allure.step('Create Helpers Instances'):
        common_elements_helper = CommonElementsHelper(browser)
        add_user_page_helper = AddUserPageHelper(browser)
        contact_list_helper = ContactListHelper(browser)
        add_contact_helper = AddContactHelper(browser)

    with allure.step('Go to adding user page'):
        add_user_page_helper.get_url(PageUrls.PAGE_ADD_USER_URL)

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

    with allure.step(f'Check if error messages are displayed'):
        error_message = add_contact_helper.get_error_message()
        assert error_message, "Error messages should be displayed for invalid inputs"
