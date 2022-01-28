from webbrowser import Chrome
from ..base_page import BasePage
from core.locator import Locator
from ..reset_password_page import ResetPasswordPage
from .sign_in_page_locators_collection import SignInPageLocatorsCollection


class SingInPage(BasePage):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__locators = SignInPageLocatorsCollection()
        self.__url = "https://cirro.io/users/sign_in"

    @property
    def url(self) -> str:
        return self.__url

    def fill_sign_in_field(self, field: str, text: str) -> None:
        self._fill_field_by_locator(self.__get_field_by_name(field), text)

    def click_on_submit_button(self) -> None:
        self._click_on_element(self.__locators.submit_button)

    def click_on_reset_password_link(self) -> ResetPasswordPage:
        self._click_on_element(self.__locators.reset_password_link)
        return ResetPasswordPage(self._driver)

    def get_alert_message(self) -> str:
        return self._get_text_by_locator(self.__locators.alert_message)

    def __get_field_by_name(self, field: str) -> Locator:
        if field == 'email':
            locator = self.__locators.user_email_field
        elif field == 'password':
            locator = self.__locators.user_password_field
        else:
            raise Exception(f"{field} not supported")
        return locator
