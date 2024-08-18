import allure
import pytest

from test_project.base_cls.validate_response import Response
from test_project.utils.api.api_users import ApiMethodsUsers
from test_project.utils.data_extractors import DataExtractor as DE

""" Author: Marie Ambrazhei """
TEST_ID = "37019186"


@pytest.fixture
def setup_method_37019186():
    response_post_user, user_password = ApiMethodsUsers.post_add_user(
        status_code=201,
        return_pass=True
    )
    response_post_user = response_post_user.json()
    user_email = DE.extract_value_by_key(response_post_user, 'email')
    user_token = DE.extract_value_by_key(response_post_user, 'token')

    response_log_out_user = ApiMethodsUsers.post_log_out_user(bearer_token=user_token)

    yield Response(response_log_out_user)

    # Delete Test Data
    user_token = ApiMethodsUsers.post_log_in_user(email=user_email, password=user_password).json()['token']
    ApiMethodsUsers.del_delete_user(bearer_token=user_token)


@allure.id(TEST_ID)
@allure.parent_suite('API')
@allure.suite('Users')
@allure.testcase("https://group-a.kaiten.ru/space/411620/card/37019186",
                 name=" POST Log Out User")
@allure.title("[Users | 37019186 ]  POST Log Out User")
@pytest.mark.api
def test_post_log_out_user_37019186(setup_method_37019186):

    response_log_out_user = setup_method_37019186

    with allure.step("Verify. Response Status Code: 200"):
        response_log_out_user.assert_status_code(200)
