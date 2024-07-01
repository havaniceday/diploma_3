import allure

from .header_page import HeaderPage
from locators import MyAccountPageLocators


class ProfilePage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MyAccountPageLocators

    @allure.step('Найти кнопку "Выход"')
    def find_exit_button(self):
        return self.wait_visibility_and_return_element(self.locator.EXIT_BUTTON)

    @allure.step('Нажать "История заказов"')
    def click_orders_history(self):
        old_url = self.get_current_url()
        self.click_on_element_by_locator(self.locator.ORDERS_HISTORY_LINK)
        self.wait_for_url_change(old_url)

    @allure.step('Нажать "Выход"')
    def click_exit_button(self):
        self.click_on_element_by_locator(self.locator.EXIT_BUTTON)

    @allure.step('Получить последний заказ из истории')
    def get_latest_order_number_from_history(self):
        return self.wait_visibility_and_return_element(self.locator.ORDER_HISTORY_LATEST)
