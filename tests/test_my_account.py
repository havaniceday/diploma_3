import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.my_account_page import ProfilePage
from data import Urls


class TestMyAccount:
    @allure.title('Переход по клику на «Личный кабинет» для незалогиненного пользователя')
    @allure.description(
        "Открывается страница логина; есть нужный URL и уникальный элемент - кнопка 'Войти'")
    def test_transition_to_login_if_anonymous(self, driver):
        home_page = HomePage(driver)
        home_page.click_my_account()
        login_page = LoginPage(driver)
        assert Urls.LOGIN == login_page.get_current_url()
        assert login_page.find_login_button() is not None

    @allure.title('Переход по клику на «Личный кабинет» для залогиненного пользователя')
    @allure.description(
        "Открывается страница аккаунта; есть нужный URL и уникальный элемент - кнопка 'Выход'")
    def test_transition_to_my_account_if_logged_in(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.click_my_account()
        profile_page = ProfilePage(driver)
        assert profile_page.find_exit_button() is not None
        assert Urls.PROFILE == profile_page.get_current_url()

    @allure.title('Переход в раздел «История заказов» для залогиненного пользователя')
    @allure.description(
        "Открывается страница истории заказов; есть нужный URL")
    def test_transition_to_history_if_logged_in(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.click_my_account()
        profile_page = ProfilePage(driver)
        profile_page.click_orders_history()
        assert Urls.HISTORY == profile_page.get_current_url()

    @allure.title('Выход из аккаунта')
    @allure.description(
        "Происходит выход из аккаунта; открывается URL логин страницы и уникальный элемент - кнопка 'Войти'")
    def test_exit_from_my_account(self, driver, get_authorized):
        home_page = HomePage(driver)
        home_page.click_my_account()
        profile_page = ProfilePage(driver)
        profile_page.click_exit_button()
        login_page = LoginPage(driver)
        assert login_page.find_login_button() is not None
        assert Urls.LOGIN == login_page.get_current_url()
