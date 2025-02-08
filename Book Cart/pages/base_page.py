from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Wrapper for selenium operations."""

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _find(self, locator: tuple) -> WebElement:
        return self._find(*locator)

    def _find_all(self, locator: tuple) -> list[WebElement]:
        return self._driver.find_elements(*locator)

    def _type(self, locator: tuple, text: str, time: int = 5):
        self._wait_until_element_is_visible(locator, time)
        field_element = self._find(locator)
        field_element.clear()
        field_element.send_keys(text)

    def _click(self, locator: tuple, time: int = 5):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _select_from_dropdown(self, dropdown_locator: tuple, option_locator: tuple, time: int = 5):
        self._wait_until_element_is_visible(dropdown_locator, time)
        self._find(dropdown_locator).click()
        self._wait_until_element_is_visible(option_locator, time)
        self._find(option_locator).click()

    def _get_text(self, locator: tuple, time: int = 5) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    @property
    def _window_handles(self) -> list[str]:
        return self._driver.window_handles

    def _switch_to_window(self, window_handle: str):
        self._driver.switch_to.window(window_handle)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 5):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))
