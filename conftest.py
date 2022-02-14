import pytest
from selenium.webdriver import Chrome
from core.config import Config
from core.domain import User
from pages import LandingPage
from core.domain import Result
from core.infrastructure.repositories import TestResultRepository

results=[]


@pytest.fixture(scope="session")
def config() -> Config:
    yield Config()


@pytest.fixture(scope="session")
def test_result_repository() -> TestResultRepository:
    yield TestResultRepository()


@pytest.fixture(scope="session")
def driver(config, test_result_repository) -> Chrome:
    driver = Chrome(config.driver_path)
    driver.get(config.host)
    driver.maximize_window()
    yield driver
    test_result_repository.save_all(
        Result.from_test_reports(
            results, 'UI'
        )
    )
    driver.quit()


@pytest.fixture
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        results.append(result)
