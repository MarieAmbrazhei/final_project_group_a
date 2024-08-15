import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.pydantic_schemas.user_schema import UserResponseSchema
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Yury Buzinau """
TEST_ID = "36995050"


@pytest.fixture
def setup_method_36995050():
    response = ApiMethodsUsers.post_add_user(status_code=201)
    token = response.json()['token']

    yield Response(response)

    ApiMethodsUsers.del_delete_user(bearer_token=token)


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/36995050",
                 name="POST Add Main User")
@allure.title("[Users | 36995050 ] POST Add Main User")
def test_post_add_main_user_36995050(setup_method_36995050):

    user_response = setup_method_36995050

    user_response.assert_status_code(201).validate(UserResponseSchema)
