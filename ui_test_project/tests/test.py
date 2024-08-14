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
    new_contact_data_1 = ApiMethodsContacts.post_add_contact(bearer_token=user_token)
    new_contact_id_1 = DE.extract_value_by_key(new_contact_data_1, "_id")

    new_contact_data_2 = ApiMethodsContacts.post_add_contact(bearer_token=user_token)
    new_contact_id_2 = DE.extract_value_by_key(new_contact_data_2, "_id")

    contact_list_data = ApiMethodsContacts.get_contact_list(bearer_token=user_token)
    time.sleep(1)
    print(len(contact_list_data))

    new_contact_data = ApiMethodsContacts.del_delete_contact(
        contact_id=new_contact_id_1,
        bearer_token=user_token)

    contact_list_data = ApiMethodsContacts.get_contact_list(bearer_token=user_token)
    time.sleep(1)
    print(len(contact_list_data))


# user_token_2 = DE.extract_value_by_key(user_data, 'token')
# user_first_name_2 = DE.extract_value_by_key(user_data, 'firstName')
# user_email_2 = DE.extract_value_by_key(user_data, 'email')
