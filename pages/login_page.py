import allure
from data import Urls
from .header_page import HeaderPage
from locators import LoginPageLocators


class LoginPage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators

    @allure.step('Нажать "Восстановить пароль"')
    def click_password_reset(self):
        self.click_on_element_by_locator(self.locator.PASSWORD_FORGOTTEN_LINK)

    @allure.step('Найти кнопку "Войти"')
    def find_login_button(self):
        return self.wait_visibility_and_return_element(self.locator.MY_LOGIN_BUTTON)

    @allure.step('Нажать "Зарегистрироваться"')
    def click_register(self):
        self.click_on_element_by_locator(self.locator.REGISTRATION_LINK)

    @allure.step('Ввести данные пользователя и нажать "Войти"')
    def login(self, email, password):
        self.fill_input(self.locator.PASSWORD_INPUT, password)
        self.fill_input(self.locator.EMAIL_INPUT, email)
        self.click_on_element_by_locator(self.locator.MY_LOGIN_BUTTON)
        self.wait_for_url_change(Urls.LOGIN)

    @allure.step("Логин с данными пользователя")
    def login_user(self, user_data):
        self.wait_page_loaded()
        self.fill_input(self.locator.EMAIL_INPUT, user_data['email'])
        self.fill_input(self.locator.PASSWORD_INPUT, user_data['password'])
        old_url = self.get_current_url()
        self.click_on_element_by_locator(self.locator.MY_LOGIN_BUTTON)
        self.wait_for_url_change(old_url)
