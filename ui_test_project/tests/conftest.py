import allure
import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browsers_chrome(request):
    browser_count = request.param

    options = Options()
    options.add_argument("--window-size=1024,768")
    options.add_argument('--disable-cache')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-blink-features=MetricsInterceptor')
    # options.add_argument("--headless=new")

    drivers = []

    logger.info(f'Start {browser_count} browsers')
    service = Service()

    for _ in range(browser_count):
        driver = webdriver.Chrome(service=service, options=options)
        drivers.append(driver)

    yield drivers

    logger.info('Close browsers')
    for driver in drivers:
        driver.close()
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            drivers = item.funcargs['browsers_chrome']
            driver = drivers[0]
            screenshot = driver.get_screenshot_as_png()

            allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
