from selenium.webdriver import Chrome


class LocalStorage:
    """This class implements all operation with local storage:
    - set value in local storage;
    - get all values from local storage;
    - get value from local storage by key;
    - get current page cookie from local storage
     """

    def __init__(self, driver: Chrome) -> None:
        self.__driver = driver

    def set_value_in_local_storage(self, name: str, value: str) -> None:
        self.__driver.execute_script(f"window.localStorage['{name}'] = '{value}';")

    def get_all_values_from_local_storage(self) -> str:
        return self.__driver.execute_script("return window.localStorage;")

    def get_value_from_local_storage(self, value: str) -> str:
        return self.__driver.execute_script(f"return window.localStorage.getItem('{value}');")

    def get_current_page_cookie_from_local_storage(self) -> str:
        return self.get_value_from_local_storage(self.__driver.current_url)
