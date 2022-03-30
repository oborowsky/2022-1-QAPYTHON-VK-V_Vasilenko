import uuid

import allure

from ui.pages.main_page import MainPage
from ui.locators import SegmentsContextTargetingPageLocators


class SegmentsContextTargetingPage(MainPage):
    locators = SegmentsContextTargetingPageLocators
    url = 'https://target.my.com/segments/context_targeting_list/'

    @allure.step('Создание нового сегмента на основе контекстного таргетинга')
    def create_context_targeting(self):
        self.click(self.locators.ADD_LIST_BUTTON_LOCATOR)
        self.send_keys(self.locators.ADD_SEARCH_WORDS_LOCATOR, "Chuchelo Myauchelo from FFXIV")
        targeting_name = str(uuid.uuid4())
        self.send_keys(self.locators.ADD_TITLE_LOCATOR, targeting_name)
        self.click(self.locators.SUBMIT_BUTTON_LOCATOR)
        self.find(self.locators.SEGMENT_CREATED_NOTIFICATION)
        return targeting_name
