from test_project.utils.api.api_users import ApiMethodsUsers


def test_test():
    user_data, user_pass = ApiMethodsUsers.post_add_user()
    print(f"{user_data=}")
