from faker import Faker
from enum import Enum


class Urls:
    BASE = 'https://stellarburgers.nomoreparties.site/'
    REGISTER = BASE + '/api/auth/register'
    LOGIN = BASE + 'login'
    FORGOT = BASE + 'forgot-password'
    DELETE = BASE + 'api/auth/user'
    HISTORY = BASE + 'account/order-history'
    PROFILE = BASE + 'account/profile'
    FEED = BASE + 'feed'


class Fakers:
    fake = Faker()
    RANDOM_EMAIL = fake.email()
    RANDOM_PASS = fake.password(6)
    RANDOM_NAME = fake.name()


class IngredientType(Enum):
    BUNS = 'buns'
    FILLINGS = 'fillings'
    SAUCE = 'sauce'
