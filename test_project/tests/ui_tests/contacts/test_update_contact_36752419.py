import allure
import pytest

from test_project.pages.add_user_page import AddUserPageHelper
from test_project.pages.common_el_page import CommonElementsHelper
from test_project.pages.contact_add_page import AddContactHelper
from test_project.pages.contact_details_page import ContactDetailsHelper
from test_project.pages.contact_edit_page import ContactEditHelper
from test_project.pages.contact_list_page import ContactListHelper
from test_project.urls.project_urls import PageUrls
from test_project.utils.constants.site_headers_names import Headers


""" Author: Yury Buzinau """
TEST_ID = "36752419"


@allure.id(TEST_ID)
@allure.parent_suite('UI Tests')
@allure.suite('Contacts')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36752419",
                 name="Update one contact")
@allure.title("[Contacts | 36752419] Update one contact")
@pytest.mark.ui
@pytest.mark.fast_ui
@pytest.mark.smoke_ui
@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_update_contact_36752419(browsers_chrome, base_ui_url):
    browser = browsers_chrome[0]

    # CREATE HELPERS INSTANCES
    common_elements_helper = CommonElementsHelper(browser)
    contact_details_helper = ContactDetailsHelper(browser)
    add_user_page_helper = AddUserPageHelper(browser)
    contact_edit_helper = ContactEditHelper(browser)
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

    with allure.step('Fill all inputs for new contact'):
        add_contact_helper.fill_contact_with_random_data()
        common_elements_helper.get_btn_submit().click()

    with allure.step(f'Check header {Headers.CONTACT_LIST}'):
        common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    with allure.step('One client appeared in the table'):
        expected_number_of_rows = 1
        actual_number_of_rows = len(contact_list_helper.get_all_table_rows())

    assert expected_number_of_rows == actual_number_of_rows, \
        (f"\nExpected number of rows: {expected_number_of_rows}"
         f"\nActual number of rows: {actual_number_of_rows}")

    with allure.step('Click on first row in the table'):
        contact_list_helper.get_all_table_rows()[0].click()

    with allure.step(f'Check header {Headers.CONTACT_DETAILS}'):
        common_elements_helper.get_page_title(Headers.CONTACT_DETAILS)

    with allure.step('Click on "Edit Contact" button'):
        contact_details_helper.get_btn_edit_contact().click()

    with allure.step(f'Check header {Headers.EDIT_CONTACT}'):
        common_elements_helper.get_page_title(Headers.EDIT_CONTACT)

    with allure.step('Refill all contact inputs'):
        contact_edit_helper.refill_contact_inputs_with_random_data(all_fields=True)
        common_elements_helper.get_btn_submit().click()

    with allure.step(f'Check header {Headers.EDIT_CONTACT}'):
        common_elements_helper.get_page_title(Headers.EDIT_CONTACT)
