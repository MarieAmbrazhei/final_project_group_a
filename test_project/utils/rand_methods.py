import random
import string
from faker import Faker

fake = Faker()


class Randoms:

    @staticmethod
    def rand_letter(length: int) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def int_gen(length: int) -> str:
        integers = string.digits
        return ''.join(random.choice(integers) for _ in range(length))

    @staticmethod
    def first_name() -> str:
        return fake.first_name()

    @staticmethod
    def last_name() -> str:
        return fake.last_name()

    @staticmethod
    def dob() -> str:
        return fake.date_of_birth().strftime('%Y-%m-%d')

    @staticmethod
    def email() -> str:
        return fake.email()

    @staticmethod
    def phone_number() -> str:
        return fake.phone_number()[:15]

    @staticmethod
    def street_address() -> str:
        return fake.street_address()

    @staticmethod
    def city() -> str:
        return fake.city()

    @staticmethod
    def state() -> str:
        return fake.state()

    @staticmethod
    def postcode() -> str:
        return fake.postcode()

    @staticmethod
    def country() -> str:
        return fake.country()
