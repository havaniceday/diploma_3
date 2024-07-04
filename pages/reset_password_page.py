import allure
from data import Fakers
from .header_page import HeaderPage
from locators import ResetPasswordLocators


class ResetPasswordPage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ResetPasswordLocators

    @allure.step('Найти кнопку "Восстановить"')
    def find_reset_button(self):
        return self.wait_visibility_and_return_element(self.locator.RESET_BUTTON)

    @allure.step('Найти кнопку "Сохранить"')
    def find_save_button(self):
        return self.wait_visibility_and_return_element(self.locator.SAVE_BUTTON)

    @allure.step('Ввести рандомный email')
    def enter_email(self):
        email = Fakers.RANDOM_EMAIL
        self.fill_input(self.locator.EMAIL_INPUT, email)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_reset_button(self):
        self.click_on_element_by_locator(self.locator.RESET_BUTTON)

    @allure.step('Ввести рандомный пароль')
    def enter_password(self):
        password = Fakers.RANDOM_PASS
        self.fill_input(self.locator.PASSWORD_INPUT, password)

    @allure.step('Кликнуть по иконке "Показать пароль"')
    def click_eye_icon(self):
        self.click_on_element_by_locator(self.locator.EYE_ICON)

    @allure.step('Получить тип поля ввода пароля')
    def get_password_input_type(self):
        return self.wait_visibility_and_return_element(self.locator.PASSWORD_INPUT).get_attribute('type')