import pytest
from selenium.webdriver.remote.webelement import WebElement
from base import BaseCase
from ui.locators import locators
from constants import *


class TestMyTarget(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        username = self.find(locators.USERNAME_LOCATOR)
        assert isinstance(username, WebElement)

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        login_button = self.find(locators.LOGIN_BUTTON_LOCATOR)
        assert isinstance(login_button, WebElement)

    @pytest.mark.UI
    def test_contacts(self):
        self.login()

        self.change_contacts(TEST_NAME1, TEST_PHONE1)
        self.driver.refresh()

        current_name = self.find(locators.FULLNAME_INPUT_LOCATOR).get_attribute('value')
        current_phone = self.find(locators.PHONE_INPUT_LOCATOR).get_attribute('value')
        first_check = (current_name == TEST_NAME1 and current_phone == TEST_PHONE1)

        self.change_contacts(TEST_NAME2, TEST_PHONE2)
        self.driver.refresh()

        current_name = self.find(locators.FULLNAME_INPUT_LOCATOR).get_attribute('value')
        current_phone = self.find(locators.PHONE_INPUT_LOCATOR).get_attribute('value')
        second_check = (current_name == TEST_NAME2 and current_phone == TEST_PHONE2)

        assert first_check and second_check

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'locator, url',
        [
            (locators.PRO_LINK_LOCATOR, "https://target.my.com/pro"),
            (locators.BILLING_LINK_LOCATOR, "https://target.my.com/billing")
        ])
    def test_navigation(self, locator, url):
        self.login()
        self.navigation(locator)
        assert self.driver.current_url == url
