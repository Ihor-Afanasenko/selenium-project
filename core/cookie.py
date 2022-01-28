from selenium.webdriver import Chrome
from core.local_storage import LocalStorage
import json


class Cookie:
    """This class saves current cookies for page and sets his in local storage with key equal url"""

    def __init__(self, driver: Chrome) -> None:
        self.__driver = driver
        self.current_cookie = self.get_all_cookies()
        LocalStorage(self.__driver).set_value_in_local_storage(f'{self.__driver.current_url}',
                                                               json.dumps(self.current_cookie))

    def set_cookies(self, cookie: dict) -> None:
        self.__driver.add_cookie(cookie)

    def get_cookie_by_name(self, name: str):
        return self.__driver.get_cookie(name)

    def get_all_cookies(self) -> list[dict]:
        return self.__driver.get_cookies()

    def remove_cookie_by_name(self, name: str) -> None:
        self.__driver.delete_cookie(name)

    def remove_all_cookies(self) -> None:
        self.__driver.delete_all_cookies()
