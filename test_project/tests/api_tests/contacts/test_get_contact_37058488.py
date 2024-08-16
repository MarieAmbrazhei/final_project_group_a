import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.contact_schema import ContactGetSchema
from test_project.utils.api.api_contacts import ApiMethodsContacts
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Maria Ambrazhei """
TEST_ID = "37058488"


@pytest.fixture
def setup_method_37058488():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_post_add_contact = ApiMethodsContacts.post_add_contact(
        bearer_token=user_token,
        status_code=201)

    contact_id = response_post_add_contact.json().get('_id')

    response_get_contact = ApiMethodsContacts.get_contact(
        bearer_token=user_token,
        status_code=200,
        contact_id=contact_id)

    yield Response(response_get_contact)

    # Delete Test Data
    ApiMethodsContacts.del_delete_contact(bearer_token=user_token, contact_id=contact_id)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Contacts')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37058488",
                 name="GET Get Contact")
@allure.title("[Contacts | 37058488 ] GET Get Contact")
def test_get_contact_37058488(setup_method_37058488):

    response_get_contact = setup_method_37058488

    with allure.step("Verify. Response Status Code: 200"):
        response_get_contact.assert_status_code(200)

    with allure.step("Verify. Response has a valid schema"):
        response_get_contact.validate(ContactGetSchema)
