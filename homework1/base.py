import pytest
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

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = (self.wait(timeout).until(EC.element_to_be_clickable(locator)))
        elem.click()

    def login(self):
        self.click(locators.LOGIN_BUTTON_LOCATOR)
        email_field = self.find(locators.EMAIL_INPUT_LOCATOR)
        email_field.send_keys(EMAIL)
        password_field = self.find(locators.PASSWORD_INPUT_LOCATOR)
        password_field.send_keys(PASSWORD)
        self.click(locators.SUBMIT_AUTH_LOCATOR)

    def logout(self):
        self.find(locators.CONTENT_LOCATOR, 10)  # Ждем прогрузки контентной части
        self.click(locators.WRAP_MENU_LOCATOR)
        self.click(locators.LOGOUT_LOCATOR)

    def change_contacts(self, name, phone):
        self.driver.get("https://target.my.com/profile/contacts")
        name_field = self.find(locators.FULLNAME_INPUT_LOCATOR)
        name_field.clear()
        name_field.send_keys(name)
        phone_field = self.find(locators.PHONE_INPUT_LOCATOR)
        phone_field.clear()
        phone_field.send_keys(phone)
        self.click(locators.SUBMIT_CONTACTS_LOCATOR)

    def navigation(self, locator):
        self.find(locators.CONTENT_LOCATOR, 10)  # Ждем прогрузки контентной части
        self.click(locator)
