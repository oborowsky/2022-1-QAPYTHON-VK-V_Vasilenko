import pytest
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import locators
from constants import EMAIL, PASSWORD


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=5):
        return WebDriverWait(self.driver, timeout=timeout)

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

    def click(self, locator, timeout=5, retry=10):
        for i in range(retry):
            try:
                elem = self.find(locator, timeout=timeout)
                elem.click()
                return
            except Exception:
                if i == retry - 1:
                    raise InvalidElementStateException

    def send_keys(self, locator, keys, timeout=5, retry=10):
        elem = self.find(locator, timeout=timeout, retry=retry)
        elem.clear()
        elem.send_keys(keys)

    def login(self):
        self.click(locators.LOGIN_BUTTON_LOCATOR)
        self.send_keys(locators.EMAIL_INPUT_LOCATOR, EMAIL)
        self.send_keys(locators.PASSWORD_INPUT_LOCATOR, PASSWORD)
        self.click(locators.SUBMIT_AUTH_LOCATOR)

    def logout(self):
        self.click(locators.WRAP_MENU_LOCATOR)
        self.click(locators.LOGOUT_LOCATOR)

    def change_contacts(self, name, phone):
        self.driver.get("https://target.my.com/profile/contacts")
        self.send_keys(locators.FULLNAME_INPUT_LOCATOR, name)
        self.send_keys(locators.PHONE_INPUT_LOCATOR, phone)
        self.click(locators.SUBMIT_CONTACTS_LOCATOR)

    def check_contacts(self, name, phone):
        current_name = self.find(locators.FULLNAME_INPUT_LOCATOR).get_attribute('value')
        current_phone = self.find(locators.PHONE_INPUT_LOCATOR).get_attribute('value')
        return current_name == name and current_phone == phone

    def navigation(self, locator):
        self.click(locator)
