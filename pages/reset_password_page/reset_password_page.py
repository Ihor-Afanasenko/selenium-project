from webbrowser import Chrome
from ..base_page import BasePage
from .reset_password_page_locators_collection import ResetPasswordPageLocatorsCollection


class ResetPasswordPage(BasePage):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__locators = ResetPasswordPageLocatorsCollection()

    def get_page_header(self) -> str:
        return self._get_text_by_locator(self.__locators.reset_header)
