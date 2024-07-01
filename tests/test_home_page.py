import allure
from pages.home_page import HomePage
from pages.feed_page import FeedPage
from data import Urls, IngredientType



class TestHomePage:
    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Происходит переход на главную страницу; есть нужный URL и уникальный элемент - раздел "Булки"')
    def test_transition_constructor(self, driver):
        home_page = HomePage(driver)
        home_page.click_my_account()
        home_page.click_constructor()
        assert home_page.find_buns_section() is not None
        assert Urls.BASE == home_page.get_current_url()

    @allure.title('Переход по клику на "Лента заказов"')
    @allure.description('Происходит переход в ленту; есть нужный URL и уникальный элемент - счетчик')
    def test_transition_orders_feed(self, driver):
        home_page = HomePage(driver)
        home_page.click_orders_feed()
        feed_page = FeedPage(driver)
        assert feed_page.find_counter() is not None
        assert Urls.FEED == feed_page.get_current_url()

    @allure.title('Клик на ингредиент')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями этого ингредиента')
    def test_detailed_window_by_ingredient_is_open(self, driver):
        home_page = HomePage(driver)
        ingredient = home_page.select_random_ingredient()
        home_page.scroll_and_click(ingredient)
        modal = home_page.get_opened_ingredient_modal()
        assert modal is not None
        assert ingredient.text.split('\n')[2] == modal.text.split('\n')[1]

    @allure.title('Клик на X в модальном окне деталей ингредиентов')
    @allure.description('Клик на X закрывает модальное окно с деталями ингредиента')
    def test_detailed_window_by_ingredient_is_closed(self, driver):
        home_page = HomePage(driver)
        ingredient = home_page.select_random_ingredient()
        home_page.scroll_and_click(ingredient)
        modal = home_page.get_opened_ingredient_modal()
        assert modal is not None
        home_page.close_opened_modal()
        modal = home_page.get_opened_ingredient_modal()
        assert modal is None

    @allure.title('Счетчик ингредиента увеличивается')
    @allure.description('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_counter_increases(self, driver):
        home_page = HomePage(driver)
        added_ingredient = home_page.add_random_ingredient_by_type(IngredientType.SAUCE)
        ingredient_count = home_page.get_ingredient_count(added_ingredient)
        assert ingredient_count == 1

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('При оформлении заказа появляется его идентификатор')
    def test_order_placement_logged_in_user_success(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.place_an_order()
        assert home_page.get_order_number_from_modal() is not None
