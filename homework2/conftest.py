import os
import pathlib

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from ui.pages.login_page import LoginPage


@pytest.fixture(scope='function')
def driver(temp_dir):
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


@pytest.fixture(scope='function')
def temp_dir(request):
    cwd_path = pathlib.Path.cwd()
    dir_path = str(pathlib.Path(cwd_path, 'tmp'))
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    node = str(request._pyfuncitem.nodeid).replace(':', '_')
    file_path = str(pathlib.Path(dir_path, node))
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    return str(file_path)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    return LoginPage(driver).login()
