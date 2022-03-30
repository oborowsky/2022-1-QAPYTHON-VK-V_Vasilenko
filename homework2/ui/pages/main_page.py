import allure

from ui.pages.base_page import BasePage
from ui.locators import MainPageLocators

class MainPage(BasePage):
    locators = MainPageLocators
    url = 'https://target.my.com/'

    @allure.step('Переход на страницу списка сегментов')
    def to_segments_list_page(self):
        from ui.pages.segments_list_page import SegmentsListPage
        self.driver.get(SegmentsListPage.url)
        return SegmentsListPage(self.driver)

    @allure.step('Переход на страницу списка компаний')
    def to_campaigns_list_page(self):
        from ui.pages.campaign_list_page import CampaignLstPage
        self.driver.get(CampaignLstPage.url)
        return CampaignLstPage(self.driver)