import allure

from ui.pages.main_page import MainPage
from ui.locators import CampaignLstPageLocators


class CampaignLstPage(MainPage):
    locators = CampaignLstPageLocators
    url = 'https://target.my.com/dashboard/'

    @allure.step('Переход на страницу создания новой компании')
    def to_campaigns_new_page(self):
        from ui.pages.campaign_new_page import CampaignNewPage
        self.driver.get(CampaignNewPage.url)
        return CampaignNewPage(self.driver)

    @allure.step('Поиск компании по заголовку: {title}')
    def find_campaign(self, title):
        return self.find(self.locators.CAMPAGN_NAME_LOCATOR(title))
