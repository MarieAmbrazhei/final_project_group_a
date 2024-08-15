from http import HTTPStatus

import allure
import requests
from loguru import logger
from retrying import retry

from test_project.urls.project_urls import ApiUrls
from test_project.utils.constants.error_msg import GlobalErrorMsg
from test_project.utils.rand_methods import Randoms


class ApiMethodsContacts:

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def post_add_contact(bearer_token: str = None,
                         first_name: str = None,
                         last_name: str = None,
                         birthdate: str = None,
                         email: str = None,
                         phone: str = None,
                         street1: str = None,
                         street2: str = None,
                         city: str = None,
                         state_province: str = None,
                         postal_code: str = None,
                         country: str = None,
                         ):
        """Available Response Keys:
        _id, firstName, lastName, birthdate, email, phone, street1, street2, city, stateProvince,
         postalCode, country, owner, __v
        """
        post_url = ApiUrls.POST_ADD_CONTACT

        try:
            with allure.step(f"API | Add Contact"):
                logger.info(f"Add Contact")

                json_data = {
                    "firstName": first_name if first_name else Randoms.first_name(),
                    "lastName": last_name if last_name else Randoms.last_name(),
                    "birthdate": birthdate if birthdate else Randoms.date_of_birth(),
                    "email": email if email else Randoms.email(),
                    "phone": phone if phone else Randoms.int_gen(length=6),
                    "street1": street1 if street1 else Randoms.street_address(),
                    "street2": street2 if street2 else Randoms.street_address(),
                    "city": city if city else Randoms.city(),
                    "stateProvince": state_province if state_province else Randoms.state(),
                    "postalCode": postal_code if postal_code else Randoms.postcode(),
                    "country": country if country else Randoms.country()
                }

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }
                response = requests.post(url=post_url, json=json_data, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.CREATED

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Add Contact. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def get_contact_list(
            bearer_token: str
    ):

        """Available Response Keys:
        _id, firstName, lastName, birthdate, email, phone, street1, street2, city, stateProvince,
         postalCode, country, owner, __v
        """
        get_url = ApiUrls.GET_CONTACT_LIST

        try:
            with allure.step(f"API | Get Contact List"):
                logger.info(f"Get Contact List")

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.get(url=get_url, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Get Contact List. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def get_contact(
            bearer_token: str,
            contact_id: str
    ):

        """Available Response Keys:
       _id, firstName, lastName, birthdate, email, phone, street1, street2, city, stateProvince,
        postalCode, country, owner, __v
        """
        get_url = ApiUrls.GET_CONTACT.format(contact_id=contact_id)

        try:
            with allure.step(f"API | Get Contact"):
                logger.info(f"Get Contact")

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.get(url=get_url, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Get Contact List. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def put_update_contact(
            bearer_token: str,
            contact_id: str,
            **kwargs
    ):
        """Available Response Keys:
        _id, firstName, lastName, birthdate, email, phone, street1, street2, city, stateProvince,
         postalCode, country, owner, __v
         \nRequired fields:
         firstName, lastName
         \nOptional fields:
         birthdate, email, phone, street1, street2, city, stateProvince,
         postalCode, country
        """

        put_url = ApiUrls.PUT_UPDATE_CONTACT.format(contact_id=contact_id)

        try:
            with allure.step(f"API | Update Contact"):
                logger.info(f"Update Contact")

                json_data = {k: v for k, v in kwargs.items() if v is not None}

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.put(url=put_url, json=json_data, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Update Contact. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def patch_update_contact(
            bearer_token: str,
            first_name: str,
            last_name: str,
            birthdate: str,
            email: str,
            phone: str,
            street1: str,
            street2: str,
            city: str,
            state_province: str,
            postal_code: str,
            country: str,
            contact_id: str
    ):
        """Available Response Keys:
        _id, firstName, lastName, birthdate, email, phone, street1, street2, city, stateProvince,
         postalCode, country, owner, __v
        """

        patch_url = ApiUrls.PATCH_UPDATE_CONTACT.format(contact_id=contact_id)

        try:
            with allure.step(f"API | Update Contact Partial"):
                logger.info(f"Update Contact Partial")

                json_data = {}
                if first_name:
                    json_data['firstName'] = first_name
                if last_name:
                    json_data['lastName'] = last_name
                if birthdate:
                    json_data['birthdate'] = birthdate
                if email:
                    json_data['email'] = email
                if phone:
                    json_data['phone'] = phone
                if street1:
                    json_data['street1'] = street1
                if street2:
                    json_data['street2'] = street2
                if city:
                    json_data['city'] = city
                if state_province:
                    json_data['stateProvince'] = state_province
                if postal_code:
                    json_data['postalCode'] = postal_code
                if country:
                    json_data['country'] = country

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }
                response = requests.patch(url=patch_url, json=json_data, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Update Contact Partial. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @staticmethod
    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def del_delete_contact(
            contact_id: str,
            bearer_token: str
    ):
        """Delete a user.
        This request sends a DELETE request to the specified endpoint to delete a user.
        """
        del_url = ApiUrls.DELETE_CONTACT.format(contact_id=contact_id)

        try:
            with allure.step(f"API | Delete Contact"):
                logger.info(f"Delete Contact")

                headers = {
                    'Authorization': f'Bearer {bearer_token}'
                }

                response = requests.delete(url=del_url, headers=headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    GlobalErrorMsg.error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Delete Contact. Status code: {act_code} ")

                return response

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise
