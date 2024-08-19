import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Marie Ambrazhei """
TEST_ID = "37019711"


@pytest.fixture
def setup_method_37019711():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_delete_user = ApiMethodsUsers.del_delete_user(
        status_code=200,
        bearer_token=user_token)

    yield Response(response_delete_user)


@allure.id(TEST_ID)
@allure.parent_suite('API')
@allure.suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37019711",
                 name="DEL Delete User")
@allure.title("[Users | 37019711 ] DEL Delete User")
@pytest.mark.api
def test_del_delete_user_37019711(setup_method_37019711):

    response_delete_user = setup_method_37019711

    with allure.step("Verify. Response Status Code: 200"):
        response_delete_user.assert_status_code(200)
