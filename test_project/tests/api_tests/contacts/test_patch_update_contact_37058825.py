import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.contact_schema import ContactUpdatePatchSchema
from test_project.utils.api.api_contacts import ApiMethodsContacts
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Maria Ambrazhei """
TEST_ID = "37058825"


@pytest.fixture
def setup_method_37058825():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_post_add_contact = ApiMethodsContacts.post_add_contact(
        bearer_token=user_token,
        status_code=201)

    contact_data = response_post_add_contact.json()
    contact_id = contact_data['_id']
    contact_data["firstName"] = "Mary"
    contact_data["lastName"] = "Puller"

    response_patch_update_contact = ApiMethodsContacts.patch_update_contact(
        status_code=200,
        bearer_token=user_token,
        contact_id=contact_id,
        **contact_data
    )

    yield Response(response_patch_update_contact)

    # Delete Test Data
    ApiMethodsContacts.del_delete_contact(bearer_token=user_token, contact_id=contact_id)
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.parent_suite('API')
@allure.suite('Contacts')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37058825",
                 name="PATCH Update Contact")
@allure.title("[Contacts | 37058825 ] PATCH Update Contact")
@pytest.mark.api
def test_patch_update_contact_37058825(setup_method_37058825):
    response_patch_update_contact = setup_method_37058825

    with allure.step("Verify. Response Status Code: 200"):
        response_patch_update_contact.assert_status_code(200)

    with allure.step("Verify. Response has a valid schema"):
        response_patch_update_contact.validate(ContactUpdatePatchSchema)
