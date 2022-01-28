from core.locator import Locator


class ContactUsPageLocatorsCollection:
    def __init__(self) -> None:
        self.form_title = Locator("//*[contains(@class,'lp-element') and @id='lp-pom-text-38']//span")
        self.first_name_field = Locator("//input[@id='first_name']")
        self.last_name_field = Locator("//input[@id='last_name']")
        self.company_field = Locator("//input[@id='company']")
        self.message_field = Locator("//*[@id='Message']")
        self.email_field = Locator("//input[@id='email']")
        self.talk_to_qa_experts_button = Locator("//*[contains(@class ,'lp-pom-button')]")
        self.terms_link = Locator("//*[contains(@id ,'lp-pom-text')]//a")
