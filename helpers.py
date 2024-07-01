from faker import Faker
import random


class SampleUserData:
    @staticmethod
    def generate_new_user():
        fake = Faker()
        payload = dict(email=f'{fake.email()}', password=f'{random.randint(10000, 9999999999)}', name=fake.name())
        return payload


class ParseHelper:
    @staticmethod
    def parse_string_to_number(s):
        try:
            number = int(s)
        except ValueError:
            raise ValueError(f"Cannot convert '{s}' to a number")
        return number
