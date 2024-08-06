import random
import string
from faker import Faker

fake = Faker()


class Randoms:

    @staticmethod
    def rand_word(length: int) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def int_gen(length: int) -> str:
        integers = string.digits
        return ''.join(random.choice(integers) for _ in range(length))

    @staticmethod
    def email_gen(length: int) -> str:
        return f"{Randoms.rand_word(length)}@mail.com"

    @staticmethod
    def date_of_birth() -> str:
        year = random.randint(1900, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 31)

        return f"{year:04d}-{month:02d}-{day:02d}"

    @staticmethod
    def generate_random_first_name() -> str:
        return fake.first_name()

    @staticmethod
    def generate_random_last_name() -> str:
        return fake.last_name()

    @staticmethod
    def generate_random_dob() -> str:
        return fake.date_of_birth().strftime('%Y-%m-%d')

    @staticmethod
    def generate_random_email() -> str:
        return fake.email()

    @staticmethod
    def generate_random_phone_number() -> str:
        return fake.phone_number()

    @staticmethod
    def generate_random_street_address() -> str:
        return fake.street_address()

    @staticmethod
    def generate_random_city() -> str:
        return fake.city()

    @staticmethod
    def generate_random_state() -> str:
        return fake.state()

    @staticmethod
    def generate_random_province() -> str:
        return fake.province()

    @staticmethod
    def generate_random_postcode() -> str:
        return fake.postcode()

    @staticmethod
    def generate_random_country() -> str:
        return fake.country()
