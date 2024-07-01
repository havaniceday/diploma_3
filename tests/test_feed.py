import allure
from pages.home_page import HomePage
from pages.feed_page import FeedPage
from pages.my_account_page import ProfilePage



class TestFeed:
    @allure.title("Клик на заказ в ленте")
    @allure.description('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_on_order_opens_order_details_modal(self, driver):
        home_page = HomePage(driver)
        home_page.click_orders_feed()
        feed_page = FeedPage(driver)
        order = feed_page.select_random_order()
        feed_page.scroll_and_click(order)
        modal = feed_page.get_opened_order_modal()
        assert modal is not None
        assert modal.text.split("\n")[0] == order.text.split("\n")[0]

    @allure.title("Заказы пользователя отображаются на странице Ленте заказов")
    @allure.description("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_present_in_feed(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.place_an_order()
        home_page.close_opened_modal()
        home_page.click_my_account()
        profile_page = ProfilePage(driver)
        profile_page.click_orders_history()
        latest_order_from_profile = profile_page.get_latest_order_number_from_history().text
        home_page.click_orders_feed()
        feed_page = FeedPage(driver)
        is_order_in_feed = feed_page.check_order_in_feed(latest_order_from_profile)
        assert is_order_in_feed == True

    @allure.title("Счётчик Выполнено за всё время увеличивается")
    @allure.description("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_user_order_increase_total_counter(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.click_orders_feed()
        feed_page = FeedPage(driver)
        latest_orders_total_counter_before = feed_page.get_total_order_counter()
        home_page.click_constructor()
        home_page.place_an_order()
        home_page.close_opened_modal()
        home_page.click_orders_feed()
        latest_orders_total_counter_after = feed_page.get_total_order_counter()
        assert latest_orders_total_counter_before < latest_orders_total_counter_after

    @allure.title("Счётчик Выполнено за сегодня увеличивается")
    @allure.description("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_user_order_increase_today_counter(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.click_orders_feed()
        feed_page = FeedPage(driver)
        latest_orders_today_counter_before = feed_page.get_today_order_counter()
        home_page.click_constructor()
        home_page.place_an_order()
        home_page.click_orders_feed()
        latest_orders_today_counter_after = feed_page.get_today_order_counter()
        assert latest_orders_today_counter_before < latest_orders_today_counter_after

    @allure.title("Номер заказа появляется в 'В работе'")
    @allure.description("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_user_order_appear_in_inprogress_feed(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.place_an_order()
        order_number = home_page.get_order_number_from_modal()
        if order_number is None:
            raise Exception("Order not created")
        home_page.close_opened_modal()
        home_page.click_orders_feed()
        feed_page = FeedPage(driver)
        order_in_progress = feed_page.get_order_in_progress(order_number)
        assert order_in_progress is not None
        assert order_in_progress == order_number
