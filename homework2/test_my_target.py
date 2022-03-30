import uuid
import pytest
from base import BaseCase
from ui.pages.login_page import LoginPage
from ui.pages.unauthorized_page import UnauthorizedPage
from static.constants import *
import allure


class TestLogin(BaseCase):

    @allure.epic("UI")
    @allure.feature("Авторизация на портале")
    @allure.story("Невалидный логин")
    @pytest.mark.UI
    def test_invalid_login(self, login_page):
        random_string = str(uuid.uuid4())
        page = login_page.login(random_string, PASSWORD)
        assert isinstance(page, LoginPage)

    @allure.epic("UI")
    @allure.feature("Авторизация на портале")
    @allure.story("Валидный логин, но невалидный пароль")
    @pytest.mark.UI
    def test_wrong_password(self, login_page):
        random_string = str(uuid.uuid4())
        page = login_page.login(EMAIL, random_string)
        assert isinstance(page, UnauthorizedPage)


class TestCampaign(BaseCase):

    @allure.epic("UI")
    @allure.feature("Рекламная кампания")
    @allure.story("Создание рекламной компании")
    @pytest.mark.UI
    def test_campaign_creation(self, main_page):
        page = main_page.to_campaigns_list_page().to_campaigns_new_page()
        title = page.create_campaign()
        page = page.to_campaigns_list_page()
        assert page.find_campaign(title)


class TestSegments(BaseCase):

    @allure.epic("UI")
    @allure.feature("Аудиторные сегменты")
    @allure.story("Создание сегмента")
    @pytest.mark.UI
    def test_segment_creation(self, main_page):
        page = main_page.to_segments_list_page().to_segments_context_targeting_page()
        title = page.create_context_targeting()
        page = page.to_segments_list_page()
        assert page.find_segment(title)

    @allure.epic("UI")
    @allure.feature("Аудиторные сегменты")
    @allure.story("Удаление сегмента")
    @pytest.mark.UI
    def test_segment_deletion(self, main_page):
        page = main_page.to_segments_list_page().to_segments_context_targeting_page()
        title = page.create_context_targeting()
        page = page.to_segments_list_page()
        page.delete_segment(title)
        assert page.find_segment(title) is None
