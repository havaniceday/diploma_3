import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.reset_password_page import ResetPasswordPage
from data import Urls


class TestPasswordReset:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description("Страница восстановления пароля открывается; есть нужный URL и уникальный элемент - кнопка 'Восстановить'")
    def test_transition_to_password_reset(self, driver):
        home_page = HomePage(driver)
        home_page.click_my_account()
        login_page = LoginPage(driver)
        login_page.click_password_reset()
        reset_page = ResetPasswordPage(driver)
        assert Urls.FORGOT == reset_page.get_current_url()
        assert reset_page.find_reset_button() is not None

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description("Появляется уникальный элемент - кнопка 'Сохранить' ")
    def test_password_reset_enter_email_and_proceed(self, driver):
        home_page = HomePage(driver)
        home_page.click_my_account()
        login_page = LoginPage(driver)
        login_page.click_password_reset()
        reset_page = ResetPasswordPage(driver)
        reset_page.enter_email()
        reset_page.click_reset_button()
        assert reset_page.find_save_button() is not None


    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description("Появляется текст, type поля ввода пароля  меняется на 'text'")
    def test_eye_iсon_changes_password_field_type(self, driver):
        home_page = HomePage(driver)
        home_page.click_my_account()
        login_page = LoginPage(driver)
        login_page.click_password_reset()
        reset_page = ResetPasswordPage(driver)
        reset_page.enter_email()
        reset_page.click_reset_button()
        reset_page.enter_password()
        old_type = reset_page.get_password_input_type()
        reset_page.click_eye_icon()
        new_type = reset_page.get_password_input_type()
        assert old_type != new_type
        assert new_type == 'text'
