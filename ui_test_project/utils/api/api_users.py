from http import HTTPStatus

import allure
import requests
from loguru import logger
from retrying import retry

from ui_test_project.urls.project_urls import ApiUrls
from ui_test_project.utils.rand_methods import Randoms


class ApiMethodsUsers:

    @staticmethod
    def _error_msg(exp_code, act_code):
        return f"Expected Status Code: {exp_code} Actual Status Code: {act_code}"

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def post_add_user(
            first_name: str = None,
            last_name: str = None,
            email: str = None,
            password: str = None
    ):
        """Available Response Keys:
        ['user']['_id'], ['user']['firstName'], ['user']['lastName'], ['user']['email'],
        ['token']
        """
        post_url = ApiUrls.POST_ADD_USER

        try:
            with allure.step(f"API | Create Main User"):
                logger.info(f"Create Main User")

                json_data = {
                    "firstName": first_name if first_name else Randoms.first_name(),
                    "lastName": last_name if last_name else Randoms.last_name(),
                    "email": email if email else Randoms.email(),
                    "password": password if password else Randoms.int_gen(10)
                }

                response = requests.post(url=post_url, json=json_data, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.CREATED

                assert act_code == exp_code, \
                    ApiMethodsUsers._error_msg(exp_code=exp_code, act_code=act_code)

                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def get_user_profile(
            bearer_token: str = None
    ):
        """Available Response Keys:
        ['_id'], ['firstName'], ['lastName'], ['email']
        """
        get_url = ApiUrls.GET_USER_PROFILE

        try:
            with allure.step(f"API | Get Main User Profile"):
                logger.info(f"Get Main User Profile")

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.get(url=get_url, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    ApiMethodsUsers._error_msg(exp_code=exp_code, act_code=act_code)

                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise


if __name__ == '__main__':
    token = ApiMethodsUsers.post_add_user()['token']
    print(ApiMethodsUsers.get_user_profile(bearer_token=token))
