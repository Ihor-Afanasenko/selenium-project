from core.locator import Locator


class ServicesPageLocatorsCollection:
    def __init__(self) -> None:
        self.talk_button = Locator("//*[contains(@class, 'button--teal')]")
