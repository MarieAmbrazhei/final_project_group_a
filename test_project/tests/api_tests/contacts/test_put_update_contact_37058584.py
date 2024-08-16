import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.contact_schema import ContactUpdateSchema
from test_project.utils.api.api_contacts import ApiMethodsContacts
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Maria Ambrazhei """
TEST_ID = "37058584 "


@pytest.fixture
def setup_method_37058584():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_post_add_contact = ApiMethodsContacts.post_add_contact(
        bearer_token=user_token,
        status_code=201)

    contact_id = response_post_add_contact.json().get('_id')

    response_put_update_contact = ApiMethodsContacts.put_update_contact(
        status_code=200,
        bearer_token=user_token,
        contact_id=contact_id,
        firstName='May',
        lastName='Miler',
        birthdate='1992-02-02',
        email='amill2er@fake.com',
        phone='8005554242',
        street1='13 School St.',
        street2='Apt. 5',
        city='Washington',
        stateProvince='QC',
        postalCode='A1A1A1',
        country='Canada',
    )

    yield Response(response_put_update_contact)

    # Delete Test Data
    ApiMethodsContacts.del_delete_contact(bearer_token=user_token, contact_id=contact_id)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Contacts')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37058584",
                 name=" PUT Update Contact")
@allure.title("[Contacts | 37058584  ]  PUT Update Contact")
def test_put_update_contact_37058584(setup_method_37058584):

    response_put_update_contact = setup_method_37058584

    with allure.step("Verify. Response Status Code: 200"):
        response_put_update_contact.assert_status_code(200)

    with allure.step("Verify. Response has a valid schema"):
        response_put_update_contact.validate(ContactUpdateSchema)
