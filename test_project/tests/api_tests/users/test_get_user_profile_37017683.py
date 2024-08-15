import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.user_schema import UserProfileResponseSchema
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Marie Ambrazhei """
TEST_ID = "37017683"


@pytest.fixture
def setup_method_37017683():
    token = ApiMethodsUsers.post_add_user(status_code=201).json().get('token')
    response = ApiMethodsUsers.get_user_profile(status_code=200, bearer_token=token)
    yield Response(response)

    ApiMethodsUsers.del_delete_user(bearer_token=token)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37017683",
                 name="GET Get User Profile")
@allure.title("[Users | 37017683 ] GET Get User Profile")
def test_get_user_profile_37017683(setup_method_37017683):

    user_response = setup_method_37017683

    user_response.assert_status_code(200).validate(UserProfileResponseSchema)
