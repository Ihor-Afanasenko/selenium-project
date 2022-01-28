from core.locator import Locator


class LandingPageLocatorsCollection:
    def __init__(self) -> None:
        self.service_menu = Locator("//*[@class='top-navigation__item-link' and normalize-space()='SERVICES']")
        self.become_tester_menu = Locator("//*[contains(@class,'footer-menu__item-link') and normalize-space()="
                                          "'Become a Tester']")
        self.sign_in_menu = Locator("//*[contains(@class,'footer-menu__item-link') and normalize-space()='Sign In']")
        self.sign_in_button = Locator("//*[contains(@class, 'button-cta--sign-in')]")
