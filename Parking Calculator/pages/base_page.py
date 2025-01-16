from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


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
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str):
        field_element = self._find(locator)
        field_element.clear()
        field_element.send_keys(text)

    def _click(self, locator: tuple):
        self._find(locator).click()

    def _select_from_dropdown(self, dropdown_locator: tuple, option_locator: tuple):
        self._find(dropdown_locator).click()
        self._find(option_locator).click()

    def _enter_date_via_widget(self, locator: tuple, date: str):
        # Check we don't have other windows open already
        assert len(self._driver.window_handles) == 1, "Too many windows/tabs opened"
        self._click(locator)
        # Store the ID of the original window
        original_window = self._driver.current_window_handle
        # Switch to new window
        # Enter the date
        # Return to the old window

    def _get_text(self, locator: tuple) -> str:
        return self._find(locator).text
