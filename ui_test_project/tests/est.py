import time

from ui_test_project.utils.api.api_contacts import ApiMethodsContacts
from ui_test_project.utils.api.api_users import ApiMethodsUsers
from ui_test_project.utils.data_extractors import DataExtractor as DE


def test_test():
    user_data, user_pass = ApiMethodsUsers.post_add_user()
    user_token = user_data['token']

    time.sleep(1)
    new_contact_data_1 = ApiMethodsContacts.post_add_contact(bearer_token=user_token)
    new_contact_id_1 = DE.extract_value_by_key(new_contact_data_1, "_id")

    new_contact_data_1['firstName'] = '11111111111'
    new_contact_data_1['lastName'] = '11111111111'
    new_contact_data_1['country'] = '11111111111'

    new_contact_data_2 = ApiMethodsContacts.post_add_contact(bearer_token=user_token)
    new_contact_id_2 = DE.extract_value_by_key(new_contact_data_2, "_id")

    contact_1 = ApiMethodsContacts.get_contact(bearer_token=user_token, contact_id=new_contact_id_1)
    ApiMethodsContacts.put_update_contact(
        bearer_token=user_token,
        contact_id=new_contact_id_1,
        **new_contact_data_1
    )

    contact_1_updated = ApiMethodsContacts.get_contact(
        bearer_token=user_token,
        contact_id=new_contact_id_1)

    print(f'{contact_1=}')
    print(f'{contact_1_updated=}')
