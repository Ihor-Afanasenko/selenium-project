from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from .singleton import Singleton
from core.locator import Locator
from core.cookie import Cookie
from core.local_storage import LocalStorage


class BasePage(Singleton):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.cookie = Cookie(self._driver)
        self.local_storage = LocalStorage(self._driver)
        self.__wait = WebDriverWait(self._driver, 15)

    def _click_on_element(self, locator: Locator) -> None:
        element = self.__wait.until(
            EC.visibility_of_element_located(
                locator.to_tuple()
            )
        )
        element.click()

    def __wait_element(self, locator: Locator) -> WebElement:
        return self.__wait.until(
            EC.presence_of_element_located(
                locator.to_tuple()
            )
        )

    def get_current_url(self) -> str:
        return self._driver.current_url

    def switch_to_second_window(self) -> None:
        window_after = self._driver.window_handles[1]
        self._driver.switch_to.window(window_after)

    def switch_to_third_window(self) -> None:
        window_after = self._driver.window_handles[2]
        self._driver.switch_to.window(window_after)

    def switch_to_first_window(self) -> None:
        window_after = self._driver.window_handles[0]
        self._driver.switch_to.window(window_after)

    def _get_text_by_locator(self, locator: Locator) -> str:
        return self.__wait.until(
            EC.visibility_of_element_located(
                locator.to_tuple()
            )
        ).text

    def _fill_field_by_locator(self, locator: Locator, text: str) -> None:
        self.__wait.until(
            EC.visibility_of_element_located(
                locator.to_tuple()
            )
        ).send_keys(text)

    def _clear_field_by_locator(self, locator: Locator) -> None:
        self.__wait.until(
            EC.visibility_of_element_located(
                locator.to_tuple()
            )
        ).clear()

    def scroll_page_to_end(self) -> None:
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
