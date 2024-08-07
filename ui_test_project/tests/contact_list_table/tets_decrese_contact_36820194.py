import allure
import pytest

from ui_test_project.pages.add_user_page import AddUserPageHelper
from ui_test_project.pages.common_el_page import CommonElementsHelper
from ui_test_project.pages.contact_add_page import AddContactHelper
from ui_test_project.pages.contact_details_page import ContactDetailsHelper
from ui_test_project.pages.contact_list_page import ContactListHelper
from ui_test_project.urls.site_page_urls import PageUrls
from ui_test_project.utils.constants.site_headers_names import Headers


@allure.suite('Contacts')
@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_decrease_contact(browsers_chrome):
    browser = browsers_chrome[0]

    with allure.step('Create Helpers Instances'):
        common_elements_helper = CommonElementsHelper(browser)
        contact_details_helper = ContactDetailsHelper(browser)
        add_user_page_helper = AddUserPageHelper(browser)
        contact_list_helper = ContactListHelper(browser)
        add_contact_helper = AddContactHelper(browser)

    with allure.step('Go to adding user page'):
        add_user_page_helper.get_url(PageUrls.PAGE_ADD_USER_URL)

    with allure.step('Create Main User'):
        add_user_page_helper.register_main_user()

    with allure.step(f'Check header {Headers.CONTACT_LIST}'):
        common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    for i in range(2):
        with allure.step('Click on button "Add new contact"'):
            contact_list_helper.get_btn_add_new_contact().click()

        with allure.step(f'Check header {Headers.ADD_CONTACT}'):
            common_elements_helper.get_page_title(Headers.ADD_CONTACT)

        with allure.step('Fill all inputs for new contact'):
            add_contact_helper.fill_contact_with_random_data()
            common_elements_helper.get_btn_submit().click()

        with allure.step(f'Check header {Headers.CONTACT_LIST}'):
            common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    with allure.step('Two contacts appeared in the table'):
        expected_number_of_rows = 2
        actual_number_of_rows = len(contact_list_helper.get_all_table_rows())

        assert expected_number_of_rows == actual_number_of_rows, \
            (f"\nExpected number of rows: {expected_number_of_rows}"
             f"\nActual number of rows: {actual_number_of_rows}")

        with allure.step('Click on first row in the table'):
            contact_list_helper.get_all_table_rows()[0].click()

        with allure.step(f'Check header {Headers.CONTACT_DETAILS}'):
            common_elements_helper.get_page_title(Headers.CONTACT_DETAILS)

        with allure.step('Click on "Delete Contact" button'):
            contact_details_helper.get_btn_delete_contact().click()

        with allure.step('Submit contact deleting'):
            contact_details_helper.confirmation_alert_confirm()

        with allure.step(f'Check header {Headers.CONTACT_LIST}'):
            common_elements_helper.get_page_title(Headers.CONTACT_LIST)

        with allure.step("Check that the total number of contacts in the list decreases by one."):
            contact_list_helper.get_all_table_rows()

        with allure.step('One contact appeared in the table'):
            expected_number_of_rows = 1
            actual_number_of_rows = len(contact_list_helper.get_all_table_rows())

            assert expected_number_of_rows == actual_number_of_rows, \
                (f"\nExpected number of rows: {expected_number_of_rows}"
                 f"\nActual number of rows: {actual_number_of_rows}")
