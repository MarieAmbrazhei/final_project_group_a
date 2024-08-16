import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.user_schema import UserResponseSchema
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Yury Buzinau """
TEST_ID = "36995050"


@pytest.fixture
def setup_method_36995050():
    response_post_user = ApiMethodsUsers.post_add_user(status_code=201)
    user_token = response_post_user.json()['token']

    yield Response(response_post_user)

    # Delete Test Data
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36995050",
                 name="POST Add Main User")
@allure.title("[Users | 36995050 ] POST Add Main User")
def test_post_add_main_user_36995050(setup_method_36995050):

    response_post_user = setup_method_36995050

    with allure.step("Verify. Response Status Code: 201"):
        response_post_user.assert_status_code(201)

    with allure.step("Verify. Response has a valid schema"):
        response_post_user.validate(UserResponseSchema)
