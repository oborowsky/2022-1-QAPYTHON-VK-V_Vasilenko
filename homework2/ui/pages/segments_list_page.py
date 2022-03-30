import allure
from selenium.common.exceptions import InvalidElementStateException

from ui.pages.main_page import MainPage
from ui.locators import SegmentsListPageLocators


class SegmentsListPage(MainPage):
    locators = SegmentsListPageLocators
    url = 'https://target.my.com/segments/segments_list/'

    @allure.step('Переход на страницу контекстного таргетинга')
    def to_segments_context_targeting_page(self):
        from ui.pages.segments_context_targeting_page import SegmentsContextTargetingPage
        self.driver.get(SegmentsContextTargetingPage.url)
        return SegmentsContextTargetingPage(self.driver)

    @allure.step('Поиск сегмента по заголовку: {title}')
    def find_segment(self, title):
        self.driver.refresh()
        try:
            return self.find(self.locators.SEGMENT_NAME_LOCATOR(title), retry=2)
        except InvalidElementStateException:
            return None

    @allure.step('Удаление сегмента с заголовком: {title}')
    def delete_segment(self, title):
        elem = self.find_segment(title)
        segment_id = elem.get_attribute('href').split('/')[-1]
        self.click(self.locators.DELETE_SEGMENT_LOCATOR(segment_id))
        self.click(self.locators.DELETE_SEGMENT_CONFIRMATION_LOCATOR)
