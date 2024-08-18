import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.user_schema import UserLogInSchema
from test_project.pydantic_schemas.user_schema import UserLogInResponseSchema
from test_project.utils.api.api_users import ApiMethodsUsers
from test_project.utils.data_extractors import DataExtractor as DE

""" Author: Yury Buzinau """
TEST_ID = "37019507"


@pytest.fixture
def setup_method_37019507():
    response_post_user, user_password = ApiMethodsUsers.post_add_user(
        status_code=201,
        return_pass=True
    )
    user_data = response_post_user.json()
    user_email = DE.extract_value_by_key(user_data, 'email')
    user_token = DE.extract_value_by_key(user_data, 'token')

    response_post_log_in_user = ApiMethodsUsers.post_log_in_user(
        email=user_email,
        password=user_password
    )

    yield Response(response_post_log_in_user)

    # Delete Test Data
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.parent_suite('API')
@allure.suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37019507",
                 name="POST Add Main User")
@allure.title("[Users | 37019507 ] POST Add Main User")
def test_post_log_in_user_37019507(setup_method_37019507):

    response_post_log_in_user = setup_method_37019507

    with allure.step("Verify. Response Status Code: 200"):
        response_post_log_in_user.assert_status_code(200)

    with allure.step("Verify. Response has a valid schema"):
        response_post_log_in_user.validate(UserLogInResponseSchema)
