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
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--headless=new")

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
