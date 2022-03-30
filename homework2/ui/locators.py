from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    USERNAME_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')
    EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[contains(@class, "authForm-module-input")][@name="email"]')
    PASSWORD_INPUT_LOCATOR = (By.XPATH, '//input[contains(@class, "authForm-module-input")][@name="password"]')
    SUBMIT_AUTH_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    ALERT_LOCATOR = (By.XPATH, '//div[contains(@class, "notify-module-error")]')


class UnauthorizedPageLocators:
    pass


class MainPageLocators:
    USERNAME_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')


class CampaignLstPageLocators:
    @staticmethod
    def CAMPAGN_NAME_LOCATOR(title):
        return (By.XPATH, f'//a[contains(@class, "nameCell-module-campaignNameLink")][contains(@title, "{title}")]')


class CampaignNewPageLocators:
    TRAFFIC_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')
    URL_INPUT_LOCATOR = (By.XPATH, '//div[contains(@class, "mainUrl-module-inputWrap")]//input')
    CAMPAGN_NAME_INPUT_LOCATOR = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//input')
    CAMPAGN_FORMAT_BANNER_LOCATOR = (
        By.XPATH, '//div[contains(@class, "banner-format-item")]//*[contains(text(),\'Баннер\')]')
    ADD_UPLOAD_BANNER_LOCATOR = (By.XPATH, '//input[contains(@data-test, "image_240x400")]')
    SAVE_UPLOAD_BANNER_LOCATOR = (By.XPATH, '//input[contains(@class, "image-cropper__save")]')
    CREATE_CAMPAING_LOCATOR = (By.XPATH, '//div[contains(@class, "js-save-button-wrap")]//button')


class SegmentsContextTargetingPageLocators:
    ADD_LIST_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "js-add-btn")]')
    ADD_SEARCH_WORDS_LOCATOR = (By.XPATH, '//textarea[contains(@class, "addForm-module-textareaNarrow")]')
    ADD_TITLE_LOCATOR = (By.XPATH, '//input[contains(@class, "input-module-input")][@data-test="newListName"]')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH,
                             '//div[contains(@class, "addForm-module-addFormPanelFooter")]//div[contains(@class, "button-module-blue")]')
    SEGMENT_CREATED_NOTIFICATION = (By.XPATH, '//div[contains(@class, "addForm-module-notifyContent")]')


class SegmentsListPageLocators:
    @staticmethod
    def SEGMENT_NAME_LOCATOR(title):
        return (By.XPATH, f'//div[contains(@class, "cells-module-nameCell")]//a[contains(@title, "{title}")]')

    @staticmethod
    def DELETE_SEGMENT_LOCATOR(id):
        return (By.XPATH, f'//div[contains(@class, "main-module-Cell")][contains(@data-test, "remove-{id}")]')

    DELETE_SEGMENT_CONFIRMATION_LOCATOR = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')
