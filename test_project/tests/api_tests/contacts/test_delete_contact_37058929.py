import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.utils.api.api_contacts import ApiMethodsContacts
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Maria Ambrazhei """
TEST_ID = "37058929"


@pytest.fixture
def setup_method_37058929():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_post_add_contact = ApiMethodsContacts.post_add_contact(
        bearer_token=user_token,
        status_code=201)

    contact_id = response_post_add_contact.json()['_id']

    response_delete_contact = ApiMethodsContacts.del_delete_contact(
        bearer_token=user_token,
        status_code=200,
        contact_id=contact_id)

    yield Response(response_delete_contact)

    # Delete Test Data
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.parent_suite('API')
@allure.suite('Contacts')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37058929",
                 name="DELETE Delete Contact")
@allure.title("[Contacts | 37058929 ] DELETE Delete Contact")
def test_del_delete_contact_37058929(setup_method_37058929):

    response_delete_contact = setup_method_37058929

    with allure.step("Verify. Response Status Code: 200"):
        response_delete_contact.assert_status_code(200)
