import pprint
import time

from ui_test_project.utils.api.api_contacts import ApiMethodsContacts
from ui_test_project.utils.api.api_users import ApiMethodsUsers
from ui_test_project.utils.data_extractors import DataExtractor as DE


def test_test():
    user_data, user_pass = ApiMethodsUsers.post_add_user()
    user_token = user_data['token']
    user_first_name = user_data['user']['firstName']
    user_email = user_data['user']['email']

    time.sleep(1)
    print(f"{user_pass=} ")
    print(f"{user_email=} ")

    new_contact_data = ApiMethodsContacts.post_add_contact(bearer_token=user_token)
    # new_contact_data = ApiMethodsUsers.get_user_profile(bearer_token=user_token)
    # new_contact_data = ApiMethodsUsers.patch_update_user(bearer_token=user_token)
    # new_contact_data = ApiMethodsUsers.post_log_out_user(bearer_token=user_token)
    # new_contact_data = ApiMethodsUsers.post_log_out_user(bearer_token=user_token)
    # new_contact_data = ApiMethodsUsers.post_log_in_user(email=user_email, password=user_pass)
    # new_contact_data = ApiMethodsUsers.del_delete_user(bearer_token=user_token)
    # new_contact_data = ApiMethodsContacts.get_contact_list(bearer_token=user_token)
    # new_contact_data = ApiMethodsContacts.get_contact(bearer_token=user_token)
    # new_contact_data = ApiMethodsContacts.get_contact(bearer_token=user_token)
    # new_contact_data = ApiMethodsContacts.put_update_contact(bearer_token=user_token)
    new_contact_data = ApiMethodsContacts.patch_update_contact(bearer_token=user_token)
    # new_contact_data = ApiMethodsContacts.del_delete_contact(bearer_token=user_token)


# user_token_2 = DE.extract_value_by_key(user_data, 'token')
# user_first_name_2 = DE.extract_value_by_key(user_data, 'firstName')
# user_email_2 = DE.extract_value_by_key(user_data, 'email')
