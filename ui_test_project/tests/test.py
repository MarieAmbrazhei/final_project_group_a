import pprint
import time

from ui_test_project.utils.api.api_contacts import ApiMethodsContacts
from ui_test_project.utils.api.api_users import ApiMethodsUsers
from ui_test_project.utils.data_extractors import DataExtractor as DE


def test_test():
    user_data, user_pass = ApiMethodsUsers.post_add_user()

    user_email = user_data['user']['email']

    time.sleep(1)
    print(f"{user_pass=} ")
    print(f"{user_email=} ")

    new_contact_data = ApiMethodsUsers.post_log_in_user(email=user_email, password=user_pass)

    # user_token_2 = DE.extract_value_by_key(user_data, 'token')
    # user_first_name_2 = DE.extract_value_by_key(user_data, 'firstName')
    # user_email_2 = DE.extract_value_by_key(user_data, 'email')

