import allure
import pytest

from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Marie Ambrazhei """
TEST_ID = "37019711"


@pytest.fixture
def setup_method_37019711():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_delete_user = ApiMethodsUsers.del_delete_user(
        status_code=200,
        bearer_token=user_token)

    yield response_delete_user


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37019711",
                 name="DEL DELETE Delete User")
@allure.title("[Users | 37019711 ] DEL DELETE Delete User")
def test_del_delete_user_37019711(setup_method_37019711):

    response_delete_user = setup_method_37019711

    with allure.step("Verify. Response Status Code: 200"):
        assert response_delete_user.status_code == 200, "Deletion failed with an error"
