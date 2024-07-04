import allure

from locators import HeaderLocators
from .base_page import BasePage


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderLocators

    @allure.step('Нажать "Лента заказов"')
    def click_orders_feed(self):
        old_url = self.get_current_url()
        self.click_on_element_by_locator(self.locator.FEED_LINK)
        self.wait_for_url_change(old_url)

    @allure.step('Нажать "Конструктор"')
    def click_constructor(self):
        old_url = self.get_current_url()
        self.click_on_element_by_locator(self.locator.CONSTRUCTOR_LINK)
        self.wait_for_url_change(old_url)

    @allure.step('Нажать "Личный Кабинет"')
    def click_my_account(self):
        old_url = self.get_current_url()
        self.click_on_element_by_locator(self.locator.MY_ACCOUNT_LINK)
        self.wait_for_url_change(old_url)
