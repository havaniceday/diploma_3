import allure

from .header_page import HeaderPage
from locators import RegisterPageLocators
from data import Fakers, Urls


class RegisterPage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = RegisterPageLocators

    @allure.step('Ввести рандомные регистрационные данные и запомнить юзера')
    def enter_reg_data_return_email_and_pass(self):
        email = Fakers.RANDOM_EMAIL
        password = Fakers.RANDOM_PASS
        name = Fakers.RANDOM_NAME
        self.fill_input(self.locator.EMAIL_INPUT, email)
        self.fill_input(self.locator.NAME_INPUT, name)
        self.fill_input(self.locator.PASSWORD_INPUT, password)
        return email, password

    @allure.step('Нажать "Зарегистрироваться"')
    def click_register(self):
        self.click_on_element_by_locator(self.locator.REGISTER_BUTTON)
        self.wait_for_url_change(Urls.REGISTER)
