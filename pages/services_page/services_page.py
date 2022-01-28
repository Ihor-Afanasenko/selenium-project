from webbrowser import Chrome
from ..base_page import BasePage
from ..contact_us_page import ContactUsPage
from .services_page_locators_collection import ServicesPageLocatorsCollection


class ServicesPage(BasePage):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__locators = ServicesPageLocatorsCollection()
        self.__url = "https://test.io/services"

    @property
    def url(self) -> str:
        return self.__url

    def select_talk_button(self) -> ContactUsPage:
        self._click_on_element(self.__locators.talk_button)
        self.switch_to_second_window()
        return ContactUsPage(self._driver)
