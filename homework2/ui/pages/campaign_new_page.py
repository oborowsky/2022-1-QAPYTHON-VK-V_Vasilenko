import os
import pathlib
import uuid
from pathlib import Path

import allure

from ui.pages.main_page import MainPage
from ui.locators import CampaignNewPageLocators


class CampaignNewPage(MainPage):
    locators = CampaignNewPageLocators
    url = 'https://target.my.com/campaign/new/'

    @allure.step('Создание новой компании')
    def create_campaign(self):
        self.click(self.locators.TRAFFIC_LOCATOR)
        self.send_keys(self.locators.URL_INPUT_LOCATOR, 'https://eu.finalfantasyxiv.com/lodestone/character/21642366/')
        company_name = str(uuid.uuid4())
        self.send_keys(self.locators.CAMPAGN_NAME_INPUT_LOCATOR, company_name)
        self.click(self.locators.CAMPAGN_FORMAT_BANNER_LOCATOR)
        script_path = os.path.dirname(os.path.abspath(__file__))
        dir_path = pathlib.Path(script_path).parents[1]
        file_path = Path(dir_path, 'static', 'files', 'my_ffxiv_character.jpg')
        banner_field = self.find(self.locators.ADD_UPLOAD_BANNER_LOCATOR, display=False)
        banner_field.send_keys(str(file_path))
        self.click(self.locators.SAVE_UPLOAD_BANNER_LOCATOR)
        self.click(self.locators.CREATE_CAMPAING_LOCATOR)
        return company_name
