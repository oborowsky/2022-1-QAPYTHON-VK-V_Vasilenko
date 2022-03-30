from ui.pages.base_page import BasePage
from ui.locators import UnauthorizedPageLocators

class UnauthorizedPage(BasePage):
    locators = UnauthorizedPageLocators
    url = 'https://account.my.com/login/?error_code=1'