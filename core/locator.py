from typing import Tuple
from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, path: str) -> None:
        self.__method = By.XPATH
        self.__path = path

    def to_tuple(self) -> Tuple[str, str]:
        return self.__method, self.__path
