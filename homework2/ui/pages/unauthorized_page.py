import allure
from ui.pages.base_page import BasePage
from ui.locators import UnauthorizedPageLocators

class UnauthorizedPage(BasePage):
    locators = UnauthorizedPageLocators
    url = 'https://account.my.com/login/?error_code=1'

    @allure.step('Поиск предупреждений при логине')
    def alert(self):
        return self.find(self.locators.ALERT_LOCATOR)
