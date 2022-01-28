import pytest
from selenium.webdriver import Chrome
from core.config import Config
from core.domain import User
from pages import LandingPage


@pytest.fixture(scope="session")
def config() -> Config:
    yield Config()


@pytest.fixture(scope="session")
def driver(config) -> Chrome:
    driver = Chrome(config.driver_path)
    driver.get(config.host)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def landing_page(driver):
    yield LandingPage(driver)


@pytest.fixture
def user() -> User:
    yield User(
        'John',
        'Dow',
        'John&John',
        'Hello world',
        'test_test@bin.do',
        'test_test.in.do',
        'qwerty'
        )
