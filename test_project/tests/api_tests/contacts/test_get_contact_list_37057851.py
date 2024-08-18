import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.contact_schema import ContactListFirstSchema
from test_project.utils.api.api_contacts import ApiMethodsContacts
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Maria Ambrazhei """
TEST_ID = "37057851"


@pytest.fixture
def setup_method_37057851():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_post_add_contact = ApiMethodsContacts.post_add_contact(
        bearer_token=user_token,
        status_code=201)

    contact_id = response_post_add_contact.json()['_id']

    response_get_contact_list = ApiMethodsContacts.get_contact_list(
        bearer_token=user_token,
        status_code=200)

    yield Response(response_get_contact_list)

    # Delete Test Data
    ApiMethodsContacts.del_delete_contact(bearer_token=user_token, contact_id=contact_id)
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.parent_suite('API')
@allure.suite('Contacts')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37057851",
                 name="GET Get Contact List")
@allure.title("[Contacts | 37057851 ] GET Get Contact List")
@pytest.mark.api
def test_get_contact_list_37057851(setup_method_37057851):

    response_get_contact_list = setup_method_37057851

    with allure.step("Verify. Response Status Code: 200"):
        response_get_contact_list.assert_status_code(200)

    with allure.step("Verify. Response has a valid schema"):
        response_get_contact_list.validate(ContactListFirstSchema)
