import time

from ui_test_project.utils.api.api_users import ApiMethodsUsers
from ui_test_project.utils.data_extractors import DataExtractor as DE


def test_test():
    user_data = ApiMethodsUsers.post_add_user()
    user_token = user_data['token']
    user_first_name = user_data['user']['firstName']
    user_email = user_data['user']['email']

    user_token_2 = DE.extract_value_by_key(user_data, 'token')
    user_first_name_2 = DE.extract_value_by_key(user_data, 'firstName')
    user_email_2 = DE.extract_value_by_key(user_data, 'email')

    time.sleep(1)

    print(f"{user_token=}")
    print(f"{user_first_name=}")
    print(f"{user_email=}")
    print('          ')
    print(f"{user_token_2=}")
    print(f"{user_first_name_2=}")
    print(f"{user_email_2=}")


