import random
import string
from faker import Faker


class Randoms:
    fake = Faker()

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

    def generate_random_first_name(self) -> str:
        return self.fake.first_name()

    def generate_random_last_name(self) -> str:
        return self.fake.last_name()

    def generate_random_dob(self) -> str:
        return self.fake.date_of_birth().strftime('%Y-%m-%d')

    def generate_random_email(self) -> str:
        return self.fake.email()

    def generate_random_phone_number(self) -> str:
        return self.fake.phone_number()

    def generate_random_street_address(self) -> str:
        return self.fake.street_address()

    def generate_random_city(self) -> str:
        return self.fake.city()

    def generate_random_state(self) -> str:
        return self.fake.state()

    def generate_random_province(self) -> str:
        return self.fake.province()

    def generate_random_postcode(self) -> str:
        return self.fake.postcode()

    def generate_random_country(self) -> str:
        return self.fake.country()

