from selenium.webdriver import Chrome


class Singleton:
    _instance = None
    _driver = None

    def __new__(cls, driver: Chrome = None):
        if not getattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: Chrome = None) -> None:
        self._driver = driver
