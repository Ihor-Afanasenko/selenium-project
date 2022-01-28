from webbrowser import Chrome
from .base_page import BasePage


class PoliciesPage(BasePage):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)

        self.__url = "https://test.io/policies"

    @property
    def url(self) -> str:
        return self.__url
