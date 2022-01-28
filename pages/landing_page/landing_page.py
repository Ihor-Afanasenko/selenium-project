from webbrowser import Chrome
from ..base_page import BasePage
from ..services_page import ServicesPage
from ..sign_in_page import SingInPage
from .landing_page_locators_collection import LandingPageLocatorsCollection


class LandingPage(BasePage):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__locators = LandingPageLocatorsCollection()

    def select_services_menu(self) -> ServicesPage:
        self._click_on_element(self.__locators.service_menu)
        return ServicesPage(self._driver)

    def get_become_a_tester_text(self) -> str:
        return self._get_text_by_locator(self.__locators.become_tester_menu)

    def select_sign_in_menu(self) -> SingInPage:
        self._click_on_element(self.__locators.sign_in_menu)
        self.switch_to_first_window()
        return SingInPage(self._driver)

    def select_sign_in_button(self) -> SingInPage:
        self._click_on_element(self.__locators.sign_in_button)
        self.switch_to_second_window()
        return SingInPage(self._driver)
