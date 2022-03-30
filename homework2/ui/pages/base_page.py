import allure
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.remote.webelement import WebElement

from ui.locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    locators = BasePageLocators
    url = 'https://target.my.com/'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=5):
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Поиск элемента с локатором: {locator}')
    def find(self, locator, timeout=5, retry=10, display=True) -> WebElement:
        for i in range(retry):
            try:
                if display:
                    return self.wait(timeout).until(EC.element_to_be_clickable(locator))
                else:
                    return self.wait(timeout).until(EC.presence_of_element_located(locator))
            except Exception:
                if i == retry - 1:
                    raise InvalidElementStateException

    @allure.step('Клик по элементу с локатором: {locator}')
    def click(self, locator, timeout=5, retry=10):
        for i in range(retry):
            try:
                elem = self.find(locator, timeout=timeout)
                elem.click()
                return
            except Exception:
                if i == retry - 1:
                    raise InvalidElementStateException

    @allure.step('Ввод данных в поле с локатором: {locator}')
    def send_keys(self, locator, keys, timeout=5, retry=10):
        elem = self.find(locator, timeout=timeout, retry=retry)
        elem.clear()
        elem.send_keys(keys)
