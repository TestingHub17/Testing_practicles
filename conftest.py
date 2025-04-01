from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--headless', default=False)


@pytest.fixture(scope="session")
def driver(request):
    headless = request.config.getoption('--headless')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    yield driver
    driver.close()


