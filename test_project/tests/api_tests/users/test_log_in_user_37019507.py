import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.user_schema import UserLogInSchema
from test_project.pydantic_schemas.user_schema import UserLogInResponseSchema
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Yury Buzinau """
TEST_ID = "37019507"


@pytest.fixture
def setup_method_37019507():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_post_log_in_user = ApiMethodsUsers.post_log_in_user(
        bearer_token=user_token,
        email='edsdasdkf@fff.com',
        password='1234567',
        status_code=200
    )
    print(response_post_log_in_user.json())
    yield Response(response_post_log_in_user)

    # Delete Test Data
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37019507",
                 name="POST Add Main User")
@allure.title("[Users | 37019507 ] POST Add Main User")
def test_post_log_in_user_37019507(setup_method_37019507):

    response_post_log_in_user = setup_method_37019507

    with allure.step("Verify. Response Status Code: 200"):
        response_post_log_in_user.assert_status_code(200)

    with allure.step("Verify. Response has a valid schema"):
        response_post_log_in_user.validate(UserLogInResponseSchema)
