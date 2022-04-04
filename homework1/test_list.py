import pytest
import uuid
from base import BaseCase
from random import randint
from ui.locators import locators


class TestMyTarget(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        assert self.find(locators.USERNAME_LOCATOR)

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        assert self.find(locators.LOGIN_BUTTON_LOCATOR)

    @pytest.mark.UI
    def test_contacts(self):
        self.login()
        name = str(uuid.uuid4())
        phone = str(randint(80000000000, 89999999999))
        self.change_contacts(name, phone)
        self.driver.refresh()
        assert self.check_contacts(name, phone)

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'navigation_locator, destination_locator',
        [
            (locators.PRO_LINK_LOCATOR, locators.SUBSCRIBE_EMAIL_LOCATOR),
            (locators.BILLING_LINK_LOCATOR, locators.SUBMIT_PAYMENT_LOCATOR)
        ])
    def test_navigation(self, navigation_locator, destination_locator):
        self.login()
        self.navigation(navigation_locator)
        assert self.find(destination_locator)
