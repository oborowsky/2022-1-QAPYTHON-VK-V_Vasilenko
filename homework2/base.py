import pytest
import os
import allure


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'browser.log', allure.attachment_type.TEXT)

            screenshot_path = os.path.join(temp_dir, 'failed.png')
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
