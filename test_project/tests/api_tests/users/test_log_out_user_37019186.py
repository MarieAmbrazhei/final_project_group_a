import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.utils.api.api_users import ApiMethodsUsers

""" Author: Marie Ambrazhei """
TEST_ID = "37019186"


@pytest.fixture
def setup_method_37019186():
    user_token = ApiMethodsUsers.post_add_user(status_code=201).json()['token']

    response_log_out_user = ApiMethodsUsers.post_log_out_user(
        status_code=200,
        bearer_token=user_token
    )
    return response_log_out_user


@allure.id(TEST_ID)
@allure.suite('API')
@allure.sub_suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37019186",
                 name=" POST Log Out User")
@allure.title("[Users | 37019186 ]  POST Log Out User")
def test_post_log_out_user_37019186(setup_method_37019186):

    response_log_out_user = setup_method_37019186

    with allure.step("Verify. Response Status Code: 200"):
        assert response_log_out_user.status_code == 200, "Logout failed with an error"

