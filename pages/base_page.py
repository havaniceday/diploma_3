import allure
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    def wait_element_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))


    def wait_page_loaded(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )

    def wait_visibility_and_return_element(self, locator):
        self.wait_element_visibility(locator)
        return self.driver.find_element(*locator)

    def wait_clickable_and_return_element(self, locator, retries=3, timeout=25):
        for attempt in range(retries):
            try:
                self.wait_element_clickable(locator, timeout)
                return self.driver.find_element(*locator)
            except StaleElementReferenceException:
                print(f"StaleElementReferenceException caught. Retrying... ({attempt + 1}/{retries})")
                if attempt == retries - 1:
                    raise Exception("Element not found or stale after retries")

        raise Exception("Failed to find clickable element after retries")

    def wait_and_return_elements(self, locator, timeout=25):
        self.wait_page_loaded(timeout=timeout)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_on_element_by_locator(self, locator):
        element = self.wait_clickable_and_return_element(locator)
        return self.driver.execute_script("arguments[0].click();", element)

    def click_on_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def drag_and_drop_element(self, source, target):
        return drag_and_drop(self.driver, source, target)

    def wait_for_url_change(self, old_url):
        return WebDriverWait(self.driver, 15).until(expected_conditions.url_changes(old_url))

    @allure.step("Получить URL текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        element = self.wait_visibility_and_return_element(locator)
        return element.text

    def fill_input(self, locator, data):
        element = self.wait_clickable_and_return_element(locator)
        element.send_keys(data)

    @allure.step("Скроллим и кликаем на элемент")
    def scroll_and_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_on_element(element)

    @allure.step("Ждем таймаут")
    def just_wait(self, timeout):
        time.sleep(timeout)
