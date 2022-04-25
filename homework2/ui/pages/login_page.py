import allure
from selenium.common.exceptions import InvalidElementStateException

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.unauthorized_page import UnauthorizedPage
from static.constants import *

from urllib.parse import urlparse

from ui.locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators
    url = 'https://target.my.com/'

    @allure.step('Логин с заданными параметрами EMAIL={email}, PASSWORD={password}')
    def login(self, email=EMAIL, password=PASSWORD):
        self.click(self.locators.LOGIN_BUTTON_LOCATOR)
        email_field = self.find(self.locators.EMAIL_INPUT_LOCATOR)
        email_field.send_keys(email)
        password_field = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        password_field.send_keys(password)
        self.click(self.locators.SUBMIT_AUTH_LOCATOR)

        try:
            if self.find(MainPageLocators.USERNAME_LOCATOR, retry=2):
                return MainPage(self.driver)
        except InvalidElementStateException:
            url = urlparse(self.driver.current_url).netloc
            if url == 'account.my.com':
                return UnauthorizedPage(self.driver)
            else:
                return self

    @allure.step('Поиск предупреждений при логине')
    def alert(self):
        return self.find(self.locators.ALERT_LOCATOR)
