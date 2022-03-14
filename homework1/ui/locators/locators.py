from selenium.webdriver.common.by import By

CONTENT_LOCATOR = ((By.XPATH, '//div[contains(@class, "layout-module-pageContentWrap")]'))

# Кнопки входа/выходы и выпадающее меню
LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
USERNAME_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')
WRAP_MENU_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-rightWrap")]')
LOGOUT_LOCATOR = (By.XPATH, '//a[contains(@class, "rightMenu-module-rightMenuLink")][@href="/logout"]')

# Форма авторизации
EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[contains(@class, "authForm-module-input")][@name="email"]')
PASSWORD_INPUT_LOCATOR = (By.XPATH, '//input[contains(@class, "authForm-module-input")][@name="password"]')
SUBMIT_AUTH_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')

# Ссылки в шапке меню
PRO_LINK_LOCATOR = (By.XPATH, '//a[contains(@class, "center-module-pro")]')
BILLING_LINK_LOCATOR = (By.XPATH, '//a[contains(@class, "center-module-billing")]')

# Форма на странице контактов
FULLNAME_INPUT_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//input')
PHONE_INPUT_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//input')
SUBMIT_CONTACTS_LOCATOR = (By.XPATH, '//button[contains(@class, "button_submit")]')
