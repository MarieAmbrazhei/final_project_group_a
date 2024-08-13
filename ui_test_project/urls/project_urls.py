class PageUrls:
    PAGE_LOGIN_URL = 'https://thinking-tester-contact-list.herokuapp.com/'
    PAGE_ADD_USER_URL = 'https://thinking-tester-contact-list.herokuapp.com/addUser'
    PAGE_CONTACT_LIST_URL = 'https://thinking-tester-contact-list.herokuapp.com/contactList'
    PAGE_ADD_CONTACT_URL = 'https://thinking-tester-contact-list.herokuapp.com/addContact'
    PAGE_CONTACT_DETAILS_URL = 'https://thinking-tester-contact-list.herokuapp.com/contactDetails'
    PAGE_EDIT_CONTACT_URL = 'https://thinking-tester-contact-list.herokuapp.com/editContact'


class ApiUrls:
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"
    POST_ADD_USER = BASE_URL + "/users"
    GET_USER_PROFILE = BASE_URL + "/users/me"
    PATCH_UPDATE_USER = BASE_URL + "/users/me"
    POST_LOGOUT_USER = BASE_URL + "/users/logout"
    POST_LOGIN_USER = BASE_URL + "/users/login"
    DELETE_USER = BASE_URL + "/users/me"
    POST_ADD_CONTACT = BASE_URL + "/contacts"
    GET_CONTACT_LIST = BASE_URL + "/contacts"
    GET_CONTACT = BASE_URL + "/contacts/"
    PUT_UPDATE_CONTACT = BASE_URL + "/contacts/"
    PATCH_UPDATE_CONTACT = BASE_URL + "/contacts/"
    DELETE_CONTACT = BASE_URL + "/contacts/"
