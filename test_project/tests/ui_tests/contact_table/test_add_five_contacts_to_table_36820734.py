import allure
import pytest
from test_project.pages.add_user_page import AddUserPageHelper
from test_project.pages.common_el_page import CommonElementsHelper
from test_project.pages.contact_add_page import AddContactHelper
from test_project.pages.contact_list_page import ContactListHelper
from test_project.urls.project_urls import PageUrls
from test_project.utils.constants.site_headers_names import Headers

""" Author: Marie Ambrazhei """
TEST_ID = "36820734"


@allure.id(TEST_ID)
@allure.parent_suite('UI Tests')
@allure.suite('Contact Table')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36820734",
                 name="Add Five Contacts To Table")
@allure.title("[Contact list | 36820734] Add Five Contacts To Table")
@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_add_five_contacts_to_table(browsers_chrome, base_ui_url):
    browser = browsers_chrome[0]

    # CREATE HELPERS INSTANCES
    common_elements_helper = CommonElementsHelper(browser)
    add_user_page_helper = AddUserPageHelper(browser)
    contact_list_helper = ContactListHelper(browser)
    add_contact_helper = AddContactHelper(browser)

    with allure.step('Go to adding user page'):
        add_user_page_helper.get_url(base_ui_url + PageUrls.PAGE_ADD_USER_URL)

    with allure.step('Create Main User'):
        add_user_page_helper.register_main_user()

    with allure.step(f'Check header {Headers.CONTACT_LIST}'):
        common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    for i in range(1, 6):
        with allure.step(f'Click on button "Add new contact" no {i}'):
            contact_list_helper.get_btn_add_new_contact().click()

        with allure.step(f'Check header {Headers.ADD_CONTACT}'):
            common_elements_helper.get_page_title(Headers.ADD_CONTACT)

        with allure.step('Fill all inputs for new contact'):
            add_contact_helper.fill_contact_with_random_data()
            common_elements_helper.get_btn_submit().click()

        with allure.step(f'Check header {Headers.CONTACT_LIST}'):
            common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    with allure.step('Five contacts appeared in the table'):
        expected_number_of_rows = 5
        actual_number_of_rows = len(contact_list_helper.get_all_table_rows())

        assert expected_number_of_rows == actual_number_of_rows, \
            (f"\nExpected number of rows: {expected_number_of_rows}"
             f"\nActual number of rows: {actual_number_of_rows}")
