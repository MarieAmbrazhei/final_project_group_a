import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.contact_schema import ContactSchema
from test_project.utils.api.api_contacts import ApiMethodsContacts
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Maria Ambrazhei """
TEST_ID = "37056725"


@pytest.fixture
def setup_method_37056725():
    response_post_user = ApiMethodsUsers.post_add_user(status_code=201).json()
    user_token = response_post_user['token']

    response_post_add_contact = ApiMethodsContacts.post_add_contact(
        bearer_token=user_token,
        status_code=201)

    contact_id = response_post_add_contact.json()['_id']

    yield Response(response_post_add_contact)

    # Delete Test Data
    ApiMethodsContacts.del_delete_contact(bearer_token=user_token, contact_id=contact_id)
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Contacts')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37056725",
                 name="POST Add contact")
@allure.title("[Contacts | 37056725 ] POST Add contact")
def test_post_add_contact_37056725(setup_method_37056725):

    response_post_add_contact = setup_method_37056725

    with allure.step("Verify. Response Status Code: 201"):
        response_post_add_contact.assert_status_code(201)

    with allure.step("Verify. Response has a valid schema"):
        response_post_add_contact.validate(ContactSchema)
