from core.locator import Locator


class SignInPageLocatorsCollection:
    def __init__(self) -> None:
        self.user_email_field = Locator("//input[@id='user_email']")
        self.user_password_field = Locator("//input[@id='user_password']")
        self.submit_button = Locator("//*[@type='submit']")
        self.alert_message = Locator("//*[@class='alert-message']")
        self.reset_password_link = Locator("//*[@class='btn-link' and normalize-space()='Reset password']")
