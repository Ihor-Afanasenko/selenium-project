from core.locator import Locator


class ResetPasswordPageLocatorsCollection:
    def __init__(self) -> None:
        self.reset_header = Locator("//*[@class='heading-divider-text']/*[@class='text-heading-3']")
