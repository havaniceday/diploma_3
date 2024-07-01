import allure
import pytest
from selenium import webdriver
from data import Urls
from helpers import SampleUserData
import requests
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--width=1280")
        firefox_options.add_argument("--height=720")
        firefox_options.add_argument('--no-sandbox')
        browser = webdriver.Firefox(options=firefox_options)
    elif request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--width=1280")
        chrome_options.add_argument("--height=720")
        chrome_options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(options=chrome_options)
    browser.get(Urls.BASE)
    try:
        yield browser
    finally:
        browser.quit()


@allure.step("Создание и удаление пользователя через апи")
@pytest.fixture()
def generate_random_user():
    user_data = SampleUserData.generate_new_user()
    response = requests.post(Urls.REGISTER, data=user_data)
    yield user_data
    headers = {'Authorization': response.json()['accessToken']}
    requests.delete(Urls.DELETE, headers=headers)


@allure.step("Логин пользователя на сайте")
@pytest.fixture()
def get_authorized(driver, generate_random_user):
    HeaderPage(driver).click_my_account()
    LoginPage(driver).login_user(generate_random_user)
