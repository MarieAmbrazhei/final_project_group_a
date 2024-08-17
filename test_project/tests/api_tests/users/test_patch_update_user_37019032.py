import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.user_schema import UserUpdateResponseSchema
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Marie Ambrazhei """
TEST_ID = "37019032"


@pytest.fixture
def setup_method_37019032():
    user_data = ApiMethodsUsers.post_add_user(status_code=201).json()
    user_token = user_data['token']
    user_info = user_data['user']

    user_info.pop('_id')
    user_info.pop('__v')
    user_info["firstName"] = "Harry"
    user_info["lastName"] = "Potter"

    response_patch_user = ApiMethodsUsers.patch_update_user(
        status_code=200,
        bearer_token=user_token,
        **user_info
    )

    yield Response(response_patch_user)

    # Delete Test Data
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37019032",
                 name="PATCH Update User")
@allure.title("[Users | 37019032 ] PATCH Update User")
def test_post_add_main_user_37019032(setup_method_37019032):

    response_patch_user = setup_method_37019032

    with allure.step("Verify. Response Status Code: 200"):
        response_patch_user.assert_status_code(200)

    with allure.step("Verify. Response has a valid schema"):
        response_patch_user.validate(UserUpdateResponseSchema)
