class PageUrls:
    BASE_URL = 'https://thinking-tester-contact-list.herokuapp.com'
    PAGE_LOGIN_URL = BASE_URL
    PAGE_ADD_USER_URL = '/addUser'
    PAGE_CONTACT_LIST_URL = '/contactList'
    PAGE_ADD_CONTACT_URL = '/addContact'
    PAGE_CONTACT_DETAILS_URL = '/contactDetails'
    PAGE_EDIT_CONTACT_URL = '/editContact'


class ApiUrls:
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"
    POST_ADD_USER = "/users"
    GET_USER_PROFILE = "/users/me"
    PATCH_UPDATE_USER = "/users/me"
    POST_LOGOUT_USER = "/users/logout"
    POST_LOGIN_USER = "/users/login"
    DELETE_USER = "/users/me"
    POST_ADD_CONTACT = "/contacts"
    GET_CONTACT_LIST = "/contacts"
    GET_CONTACT = "/contacts/{contact_id}"
    PUT_UPDATE_CONTACT = "/contacts/{contact_id}"
    PATCH_UPDATE_CONTACT = "/contacts/{contact_id}"
    DELETE_CONTACT = "/contacts/{contact_id}"
