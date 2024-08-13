import pprint
from http import HTTPStatus

import allure
import requests
from loguru import logger
from retrying import retry

from ui_test_project.urls.project_urls import ApiUrls
from ui_test_project.utils.rand_methods import Randoms
from ui_test_project.utils.api.api_users import ApiMethodsUsers


class ApiMethodsContacts:
    token = ApiMethodsUsers.post_add_user().get("token")
    headers = {
        'Authorization': f'Bearer {token}'
    }
    email = None
    first_name = None
    @staticmethod
    def _error_msg(exp_code, act_code):
        return f"Expected Status Code: {exp_code} Actual Status Code: {act_code}"

    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def post_add_contact(self,
                         first_name: str = None,
                         last_name: str = None,
                         birthdate: str = None,
                         email: str = None,
                         phone: str = None,
                         street1: str = None,
                         street2: str = None,
                         city: str = None,
                         stateProvince: str = None,
                         postalCode: str = None,
                         country: str = None,
                         ):
        """Available Response Keys:
        ['contact']['_id'], ['contact']['firstName'], ['contact']['lastName'],
        ['contact'] ['birthdate'], ['contact']['email'], ['contact']['phone'],
        ['contact']['street1'],['contact']['street2'],['contact']['city'],
        ['contact']['stateProvince'], ['contact']['postalCode'], ['contact']['country'],
        ['contact']['owner'], ['contact']['__v']
        """
        post_url = ApiUrls.POST_ADD_CONTACT
        self.email = email if email else Randoms.email()
        self.first_name = first_name if first_name else Randoms.first_name()
        try:
            with allure.step(f"API | Add Contact"):
                logger.info(f"Add Contact")

                json_data = {
                    "firstName": self.first_name,
                    "lastName": last_name if last_name else Randoms.last_name(),
                    "birthdate": birthdate if birthdate else Randoms.date_of_birth(),
                    "email": self.email,
                    "phone": phone if phone else Randoms.int_gen(length=6),
                    "street1": street1 if street1 else Randoms.street_address(),
                    "street2": street2 if street2 else Randoms.street_address(),
                    "city": city if city else Randoms.city(),
                    "stateProvince": stateProvince if stateProvince else Randoms.state(),
                    "postalCode": postalCode if postalCode else Randoms.postcode(),
                    "country": country if country else Randoms.country()
                }
                response = requests.post(url=post_url, headers=self.headers, json=json_data,
                                         timeout=5)

                act_code = response.status_code
                exp_code = HTTPStatus.CREATED

                assert act_code == exp_code, \
                    ApiMethodsContacts._error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Add Contact. Status code: {act_code} ")
                pprint.pprint(response.json())
                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def get_contact_list(self):

        """Available Response Keys:
        ['contact']['_id'], ['contact']['firstName'], ['contact']['lastName'],
        ['contact'] ['birthdate'], ['contact']['email'], ['contact']['phone'],
        ['contact']['street1'],['contact']['street2'],['contact']['city'],
        ['contact']['stateProvince'], ['contact']['postalCode'], ['contact']['country'],
        ['contact']['owner'], ['contact']['__v']
        """
        get_url = ApiUrls.GET_CONTACT_LIST

        try:
            with allure.step(f"API | Get Contact List"):
                logger.info(f"Get Contact List")

                response = requests.get(url=get_url, headers=self.headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    ApiMethodsContacts._error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Get Contact List. Status code: {act_code} ")
                pprint.pprint(response.json())
                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def get_contact(self):

        """Available Response Keys:
        ['contact']['_id'], ['contact']['firstName'], ['contact']['lastName'],
        ['contact'] ['birthdate'], ['contact']['email'], ['contact']['phone'],
        ['contact']['street1'],['contact']['street2'],['contact']['city'],
        ['contact']['stateProvince'], ['contact']['postalCode'], ['contact']['country'],
        ['contact']['owner'], ['contact']['__v']
        """
        get_url = ApiUrls.GET_CONTACT

        try:
            with allure.step(f"API | Get Contact"):
                logger.info(f"Get Contact")

                response = requests.get(url=get_url, headers=self.headers, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    ApiMethodsContacts._error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Get Contact List. Status code: {act_code} ")
                pprint.pprint(response.json())
                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def put_update_contact(self,
                           first_name: str = None,
                           last_name: str = None,
                           birthdate: str = None,
                           email: str = None,
                           phone: str = None,
                           street1: str = None,
                           street2: str = None,
                           city: str = None,
                           stateProvince: str = None,
                           postalCode: str = None,
                           country: str = None,
                           ):
        """Available Response Keys:
        ['contact']['_id'], ['contact']['firstName'], ['contact']['lastName'],
        ['contact'] ['birthdate'], ['contact']['email'], ['contact']['phone'],
        ['contact']['street1'],['contact']['street2'],['contact']['city'],
        ['contact']['stateProvince'], ['contact']['postalCode'], ['contact']['country'],
        ['contact']['owner'], ['contact']['__v']
        """

        put_url = ApiUrls.PUT_UPDATE_CONTACT
        print(self.email)
        print(self.first_name)
        print("*" * 100)
        try:
            with allure.step(f"API | Update Contact"):
                logger.info(f"Update Contact")

                json_data = {
                    "firstName": self.first_name,
                    "lastName": last_name if last_name else Randoms.last_name(),
                    "birthdate": birthdate if birthdate else Randoms.date_of_birth(),
                    "email": self.email,
                    "phone": phone if phone else Randoms.int_gen(length=6),
                    "street1": street1 if street1 else Randoms.street_address(),
                    "street2": street2 if street2 else Randoms.street_address(),
                    "city": city if city else Randoms.city(),
                    "stateProvince": stateProvince if stateProvince else Randoms.state(),
                    "postalCode": postalCode if postalCode else Randoms.postcode(),
                    "country": country if country else Randoms.country()
                }

                response = requests.put(url=put_url, json=json_data, headers=self.headers,
                                        timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    ApiMethodsContacts._error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Update Contact. Status code: {act_code} ")
                pprint.pprint(response.json())
                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def patch_update_contact(self,
                             first_name: str = None,
                             ):
        """Available Response Keys:
        ['contact']['_id'], ['contact']['firstName'], ['contact']['lastName'],
        ['contact'] ['birthdate'], ['contact']['email'], ['contact']['phone'],
        ['contact']['street1'],['contact']['street2'],['contact']['city'],
        ['contact']['stateProvince'], ['contact']['postalCode'], ['contact']['country'],
        ['contact']['owner'], ['contact']['__v']
        """

        patch_url = ApiUrls.PATCH_UPDATE_CONTACT

        try:
            with allure.step(f"API | Update Contact Partial"):
                logger.info(f"Update Contact Partial")

                json_data = {
                    "firstName": self.first_name if not first_name else None,
                }
                print(json_data)
                print("8" * 100)
                response = requests.patch(url=patch_url, json=json_data, headers=self.headers,
                                          timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    ApiMethodsContacts._error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Update Contact Partial. Status code: {act_code} ")
                pprint.pprint(response.json())
                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise

    @retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
    def del_delete_contact(self,
                           bearer_token: str = None
                           ):
        """Delete a user.
        This request sends a DELETE request to the specified endpoint to delete a contact.
        """

        del_url = ApiUrls.DELETE_CONTACT

        try:
            with allure.step(f"API | Delete Contact"):
                logger.info(f"DDelete Contact")

                response = requests.delete(url=del_url, headers=self.headers, json={}, timeout=5)
                act_code = response.status_code
                exp_code = HTTPStatus.OK

                assert act_code == exp_code, \
                    ApiMethodsContacts._error_msg(exp_code=exp_code, act_code=act_code)
                logger.success(f"Delete Contact. Status code: {act_code} ")

                return response.json()

        except Exception as e:
            logger.warning(f"Error while executing the request: {str(e)}")
            raise


if __name__ == '__main__':
    contacts = ApiMethodsContacts()
    contacts.post_add_contact()
    contacts.get_contact_list()
    contacts.get_contact()
    # contacts.put_update_contact()
    # contacts.patch_update_contact()
    # contacts.del_delete_contact()
