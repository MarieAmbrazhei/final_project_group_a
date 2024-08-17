import requests
from loguru import logger

from test_project.utils.constants.error_msg import GlobalErrorMsg


class Response:

    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code

        # Log request information
        logger.info(f"Request URL: {response.request.method} {response.request.url}")

        # Log response status
        logger.info(f"Response Status: {self.response_status}")

        try:
            self.response_json = response.json()
            logger.info('Response contains JSON data.')
        except requests.exceptions.JSONDecodeError:
            self.response_json = None
            logger.warning("Response doesn't contain JSON data.")

    def validate(self, schema):
        logger.info('Validating response against schema...')

        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)

        logger.success('Response validation completed.')
        return self

    def assert_status_code(self, status_code):
        logger.info(f"Asserting response status code, expected: {status_code}, "
                    f"actual: {self.response_status}")

        if isinstance(status_code, list):
            assert self.response_status in status_code, \
                GlobalErrorMsg.error_msg(exp_code=status_code, act_code=self.response_status)
        else:
            assert self.response_status == status_code, \
                GlobalErrorMsg.error_msg(exp_code=status_code, act_code=self.response_status)

        logger.success('Status code assertion passed.')
        return self
