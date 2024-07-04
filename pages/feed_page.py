import allure

from .header_page import HeaderPage
from locators import FeedPageLocators
from helpers import ParseHelper
import random
from selenium.common.exceptions import TimeoutException


class FeedPage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = FeedPageLocators

    @allure.step('Найти счетчик')
    def find_counter(self):
        return self.wait_visibility_and_return_element(self.locator.ALL_TIME_COUNTER)

    @allure.step('Выбор рандомного заказа')
    def select_random_order(self):
        orders = self.wait_and_return_elements(self.locator.ORDERS_LIST)
        order = random.choice(orders)
        self.wait_element_clickable(order)
        return order

    @allure.step('Проверка что заказ отображается в списке заказов')
    def check_order_in_feed(self, order_str):
        order_number_elements = self.wait_and_return_elements(self.locator.ORDERS_NUMBERS_LIST)
        order_num_text = [number_element.text for number_element in order_number_elements]
        return order_str in order_num_text

    @allure.step('Получение списка заказов в рабsоте')
    def get_order_in_progress(self, order_number):

        order_number_element = self.wait_visibility_and_return_element((self.locator.ORDER_NUMBER_IN_IN_PROGRESS[0],
                                                                        self.locator.ORDER_NUMBER_IN_IN_PROGRESS[1].format(order_number)))

        if not order_number_element:
            return None
        return order_number_element.text.lstrip("0")

    def get_opened_order_modal(self):
        try:
            opened_modal = self.wait_visibility_and_return_element(self.locator.ORDER_MODAL_DESCRIPTION)
            return opened_modal
        except TimeoutException:
            return None

    @allure.step('Получить значение общего счетчика заказов')
    def get_total_order_counter(self):
        orders_total = self.wait_visibility_and_return_element(self.locator.ORDERS_TOTAL)
        return ParseHelper.parse_string_to_number(orders_total.text)

    @allure.step('Получить значение счетчика заказов за сегодня')
    def get_today_order_counter(self):
        orders_today = self.wait_visibility_and_return_element(self.locator.ORDERS_TODAY)
        return ParseHelper.parse_string_to_number(orders_today.text)
