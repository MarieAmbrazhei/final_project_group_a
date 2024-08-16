import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.user_schema import UserResponseSchema
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Yury Buzinau """
TEST_ID = "36995050"


@pytest.fixture
def setup_method_36995050():
    response_add_user = ApiMethodsUsers.post_add_user(status_code=201).json()
    user_token = response_add_user['token']

    yield Response(user_token)

    # Delete Test Data
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36995050",
                 name="POST Add Main User")
@allure.title("[Users | 36995050 ] POST Add Main User")
def test_post_add_main_user_36995050(setup_method_36995050):

    user_response = setup_method_36995050

    with allure.step("Verify. Response Status Code: 201"):
        user_response.assert_status_code(201)

    with allure.step("Verify. Response has a valid schema"):
        user_response.validate(UserResponseSchema)
