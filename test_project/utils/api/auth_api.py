import os

import requests
from dotenv import load_dotenv
from loguru import logger
from retrying import retry

from test_project.urls.project_urls import ApiUrls

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env'))


def get_credentials():
    username = os.getenv('MAIN_USER_EMAIL')
    password = os.getenv('MAIN_USER_PASS')

    if username is None or password is None:
        raise ValueError("Username or password not found in the environment variables.")

    return {"email": username, "password": password}


class ApiMethodsAuthentication:
    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=10)
    def set_token_into_session():
        post_url = ApiUrls.POST_LOGIN_USER
        try:
            auth_data = get_credentials()

            session = requests.Session()
            response = session.post(url=post_url, json=auth_data)

            logger.info(response)

            token = response.json()['token']
            session.headers.update({"authorization": f"Bearer {token}"})
            return session

        except Exception as e:
            logger.error(f"Error while executing the request: {str(e)}")
            raise


if __name__ == '__main__':
    ApiMethodsAuthentication.set_token_into_session()
