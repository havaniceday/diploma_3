import allure
import random
from .header_page import HeaderPage
from data import IngredientType
from locators import HomePageLocators
from selenium.common.exceptions import TimeoutException


class HomePage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Найти раздел "Булки"')
    def find_buns_section(self):
        return self.wait_visibility_and_return_element(HomePageLocators.BUNS_TAB)

    @allure.step('Выбор рандомного ингредиента')
    def select_random_ingredient(self):
        ingredients = self.wait_and_return_elements(HomePageLocators.INGREDIENTS_LIST)
        ingredient = random.choice(ingredients)
        return ingredient

    @allure.step('Выбор ингредиента по типу')
    def select_ingredient_by_type(self, ingredient_type):
        locator_map = {
            IngredientType.BUNS: HomePageLocators.INGREDIENTS_LIST_BUNS,
            IngredientType.FILLINGS: HomePageLocators.INGREDIENTS_LIST_FILLINGS,
            IngredientType.SAUCE: HomePageLocators.INGREDIENTS_LIST_SAUCE
        }

        if ingredient_type not in locator_map:
            raise ValueError(f"Unsupported ingredient type: {ingredient_type}")

        elements = self.wait_and_return_elements(locator_map[ingredient_type])
        return random.choice(elements)

    @allure.step('Найти открытое модальное окно ингредиента')
    def get_opened_ingredient_modal(self, timeout=15):
        try:
            opened_modal = self.wait_visibility_and_return_element(HomePageLocators.INGREDIENT_MODAL_DESCRIPTION, timeout)
            return opened_modal
        except TimeoutException:
            return None

    @allure.step('Закрыть модальное окно')
    def close_opened_modal(self):
        close_button = self.wait_visibility_and_return_element(HomePageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)
        self.click_on_element(close_button)

    @allure.step('Добавить ингридиент в бургер')
    def add_random_ingredient(self):
        ingredient = self.select_random_ingredient()
        order_cart = self.wait_visibility_and_return_element(HomePageLocators.ORDER_CART)
        self.drag_and_drop_element(ingredient, order_cart)
        return ingredient

    @allure.step('Добавить ингридиент в бургер')
    def add_random_ingredient_by_type(self, ingredient_type):
        ingredient = self.select_ingredient_by_type(ingredient_type)
        order_cart = self.wait_visibility_and_return_element(HomePageLocators.ORDER_CART)
        self.drag_and_drop_element(ingredient, order_cart)
        return ingredient


    @allure.step('Вернуть часть текста со счетчиком с добавленного элемента')
    def get_ingredient_count(self, ingredient):
        return int(ingredient.text.split('\n')[0])

    def order_now(self):
        self.click_on_element_by_locator(HomePageLocators.ORDER_BUTTON)
        self.wait_visibility_and_return_element(HomePageLocators.INGREDIENT_MODAL_DESCRIPTION)

    @allure.step('Создать и оформить заказ')
    def place_an_order(self):
        self.add_random_ingredient_by_type(IngredientType.BUNS)
        self.add_random_ingredient_by_type(IngredientType.FILLINGS)
        self.add_random_ingredient_by_type(IngredientType.SAUCE)
        self.order_now()

    @allure.step("Получить номер заказа")
    def get_order_number_from_modal(self, retries=5, timeout=2):
        for attempt in range(retries):
            try:
                self.just_wait(timeout)
                order = self.get_text(HomePageLocators.ORDER_NUMBER)
                if order == '9999':
                    raise ValueError("Order number not populated yet")
                return order
            except ValueError:
                print(f"Retrying get_order_number_from_modal... ({attempt + 1}/{retries})")
                if attempt == retries - 1:
                    return None
