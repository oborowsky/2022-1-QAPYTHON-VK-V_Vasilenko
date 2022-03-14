import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    url = 'https://target.my.com/'
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("prefs",
                                    {"profile.default_content_setting_values.notifications": 2
                                     })
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    driver.delete_all_cookies()
    driver.get(url)
    yield driver
    driver.quit()
