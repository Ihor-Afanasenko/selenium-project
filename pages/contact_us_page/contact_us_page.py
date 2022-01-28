from webbrowser import Chrome
from ..base_page import BasePage
from ..policies_page import PoliciesPage
from core.locator import Locator
from .contact_us_locators_page_collection import ContactUsPageLocatorsCollection


class ContactUsPage(BasePage):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__locators = ContactUsPageLocatorsCollection()
        self.__url = "https://hi.test.io/contact-us/"

    @property
    def url(self):
        return self.__url

    def get_form_title(self) -> str:
        return self._get_text_by_locator(self.__locators.form_title)

    def fill_form_field(self, field: str, value: str) -> None:
        element = self.__get_field_locator_by_name(field)
        self._fill_field_by_locator(element, value)

    def __get_field_locator_by_name(self, field: str) -> Locator:
        if field == 'first name':
            locator = self.__locators.first_name_field
        elif field == 'last name':
            locator = self.__locators.last_name_field
        elif field == 'company':
            locator = self.__locators.company_field
        elif field == 'message':
            locator = self.__locators.message_field
        elif field == 'email':
            locator = self.__locators.email_field
        else:
            raise Exception(f"{field} not support")
        return locator

    def clear_field_by_name(self, field: str) -> None:
        locator = self.__get_field_locator_by_name(field)
        self._clear_field_by_locator(locator)

    def click_on_talk_to_qa_experts_button(self) -> None:
        self._click_on_element(self.__locators.talk_to_qa_experts_button)

    def click_on_term_link(self) -> PoliciesPage:
        self._click_on_element(self.__locators.terms_link)
        self.switch_to_third_window()
        return PoliciesPage(self._driver)
