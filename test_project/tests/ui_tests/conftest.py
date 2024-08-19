import allure
import pytest
from loguru import logger

from test_project.urls.project_urls import PageUrls


@pytest.fixture
def base_ui_url():
    return PageUrls.BASE_URL


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            drivers = item.funcargs['browsers_chrome']
            driver = drivers[0]
            screenshot = driver.get_screenshot_as_png()
            logger.success("Screenshot Created")

            allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
