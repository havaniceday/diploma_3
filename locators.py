from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    RESET_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    SAVE_BUTTON = By.XPATH, './/button[text()="Сохранить"]'
    EMAIL_INPUT = By.XPATH, './/input[@name="name"]'
    PASSWORD_INPUT = By.XPATH, './/label[text()="Пароль"]/parent::div/input'
    EYE_ICON = By.XPATH, './/div[@class="input__icon input__icon-action"]'


class LoginPageLocators:
    PASSWORD_FORGOTTEN_LINK = (
        By.XPATH, "//a[contains(@href, '/forgot-password')]")  # ссылка на восстановление забытого пароля
    MY_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGISTRATION_LINK = (By.XPATH, "//a[contains(@href, '/register')]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][name='Пароль']")  # поле ввода пароля
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")  # поле ввода email


class RegisterPageLocators:
    EMAIL_INPUT = (By.XPATH, "(.//label[text()='Email']/following::input)[1]")  # поле ввода email
    NAME_INPUT = (By.XPATH, "(.//label[text()='Имя']/following::input)[1]")  # поле имени
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][name='Пароль']")  # поле ввода пароля
    REGISTER_BUTTON = (
        By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # финальная кнопка для завершения регистрации


class MyAccountPageLocators:
    EXIT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"
    ORDERS_HISTORY_LINK = By.XPATH, "//a[text()='История заказов']"
    ORDER_HISTORY_LATEST = By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[1]//p[@class='text text_type_digits-default']"


class HomePageLocators:
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab') and descendant::span[contains(text(), 'Булки')]]")
    INGREDIENTS_LIST = (By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients")]//a[contains(@class, "BurgerIngredient_ingredient")]')
    INGREDIENTS_LIST_BUNS = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]//h2[text()='Булки']/following-sibling::ul[1]//a")
    INGREDIENTS_LIST_FILLINGS = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]//h2[text()='Начинки']/following-sibling::ul[1]//a")
    INGREDIENTS_LIST_SAUCE = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]//h2[text()='Соусы']/following-sibling::ul[1]//a")
    INGREDIENT_MODAL_DESCRIPTION = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]")
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_CART = (By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]//p[text()="идентификатор заказа"]/preceding-sibling::h2')


class HeaderLocators:
    MY_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")  # перейти на страницу авторизации
    FEED_LINK = (By.XPATH, "//a[contains(@href, '/feed')]")  # переход в ленту заказов
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header') and @href = '/']")  # переход в конструктор


class FeedPageLocators:
    ALL_TIME_COUNTER = By.XPATH, '(.//p[contains(@class, "OrderFeed_number")])[1]'
    ORDERS_LIST = By.XPATH, '(.//li[contains(@class, "OrderHistory_listItem")]/a[contains(@class, "OrderHistory")])'
    ORDERS_NUMBERS_LIST = By.XPATH, "//div[contains(@class, 'OrderHistory_textBox')]//p[contains(@class, 'text_type_digits-default')]"
    ORDER_NUMBER_IN_IN_PROGRESS = (By.XPATH, '//p[text()="В работе:"]/following-sibling::ul[2]/li[text()="{}"]')
    ORDERS_IN_PROGRESS_NUMBERS_LIST = (By.XPATH,'//p[text()="В работе:"]/following-sibling::ul[2]/li[not(text()="Все текущие заказы готовы!")]')
    ORDER_MODAL_DESCRIPTION = (By.XPATH, ".//section[contains(@class,'Modal_modal_opened')]/div[contains(@class,'Modal_modal__container')]")
    ORDERS_TOTAL = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    ORDERS_TODAY = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"
