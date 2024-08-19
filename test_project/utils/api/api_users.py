from http import HTTPStatus

import allure
import requests
from loguru import logger
from retrying import retry

from test_project.urls.project_urls import ApiUrls
from test_project.utils.constants.error_msg import GlobalErrorMsg
from test_project.utils.rand_methods import Randoms


class ApiMethodsUsers:

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def post_add_user(
            *,
            first_name: str = None,
            last_name: str = None,
            email: str = None,
            password: str = None,
            status_code: int = HTTPStatus.CREATED,
            return_pass: bool = False
    ):
        """Available Response Keys:
        _id, firstName, lastName, email, __v, token
        """
        post_url = ApiUrls.BASE_URL + ApiUrls.POST_ADD_USER

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
                exp_code = status_code

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Add User. Status code: {act_code} ")

                if return_pass:
                    return response, json_data['password']
                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def get_user_profile(
            *,
            bearer_token: str,
            status_code: int = HTTPStatus.OK,
    ):
        """Available Response Keys:
        _id, firstName, lastName, email, __v
        """
        get_url = ApiUrls.BASE_URL + ApiUrls.GET_USER_PROFILE

        try:
            with allure.step(f"API | Get Main User Profile"):
                logger.info(f"Get Main User Profile")

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.get(url=get_url, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = status_code

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Get User Profile. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def patch_update_user(
            *,
            bearer_token: str,
            status_code: int = HTTPStatus.OK,
            **kwargs
    ):
        """Available Response Keys:
        _id, firstName, lastName, email, __v, token
        \nRequired fields:
         firstName, lastName, email, password
        """

        patch_url = ApiUrls.BASE_URL + ApiUrls.PATCH_UPDATE_USER

        try:
            with allure.step("API | Update User"):
                logger.info("Update User")

                json_data = {k: v for k, v in kwargs.items()}

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.patch(url=patch_url, headers=headers, json=json_data, timeout=5)
                act_code = response.status_code
                exp_code = status_code

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Update user. Status code: {act_code}")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def post_log_out_user(
            *,
            bearer_token: str,
            status_code: int = HTTPStatus.OK
    ):
        """Log out user from the system.
        The response should indicate success without necessarily returning user information.
        """
        log_out_url = ApiUrls.BASE_URL + ApiUrls.POST_LOGOUT_USER

        try:
            with allure.step(f"API | User Log Out"):
                logger.info(f"User Log Out")

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.post(url=log_out_url, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = status_code

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"User log Out. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def post_log_in_user(
            *,
            email: str = None,
            password: str = None,
            status_code: int = HTTPStatus.OK
    ):
        """Available Response Keys:
        _id, firstName, lastName, email, __v, token
        """
        log_in_url = ApiUrls.BASE_URL + ApiUrls.POST_LOGIN_USER

        try:
            with allure.step(f"API | Log In User"):
                logger.info(f"Log In User")

                json_data = {
                    "email": email,
                    "password": password
                }

                response = requests.post(url=log_in_url, json=json_data, timeout=5)
                act_code = response.status_code
                exp_code = status_code

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)

                logger.success(f"Log In User. Status code: {act_code} ")
                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def del_delete_user(
            *,
            bearer_token: str,
            status_code: int = HTTPStatus.OK
    ):
        """Delete a user.
        This request sends a DELETE request to the specified endpoint to delete a user.
        """
        del_url = ApiUrls.BASE_URL + ApiUrls.DELETE_USER

        try:
            with allure.step(f"API | Delete User"):
                logger.info(f"Delete User")

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.delete(url=del_url, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = status_code

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Delete User. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise
