from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Wrapper for selenium operations."""

    def __init__(self, driver: WebDriver):
        """Initialize the base page with a WebDriver instance."""
        self._driver = driver

    def _open_url(self, url: str):
        """Open the specified URL in the browser."""
        self._driver.get(url)

    def _is_displayed(self, locator: tuple) -> bool:
        """Check if an element is displayed on the page."""
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _find(self, locator: tuple) -> WebElement:
        """Find and return a single web element."""
        return self._driver.find_element(*locator)

    def _find_all(self, locator: tuple) -> list[WebElement]:
        """Find and return a list of matching web elements."""
        return self._driver.find_elements(*locator)

    def _type(self, locator: tuple, text: str, time: int = 5):
        """Type text into an input field after clearing it."""
        self._wait_until_element_is_visible(locator, time)
        field_element = self._find(locator)
        field_element.clear()
        field_element.send_keys(text)

    def _click(self, locator: tuple, time: int = 5):
        """Click on an element after ensuring its visibility."""
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _select_from_dropdown(self, dropdown_locator: tuple, option_locator: tuple, time: int = 5):
        """Select an option from a dropdown menu."""
        self._wait_until_element_is_visible(dropdown_locator, time)
        self._find(dropdown_locator).click()
        self._wait_until_element_is_visible(option_locator, time)
        self._find(option_locator).click()

    def _get_text(self, locator: tuple, time: int = 5) -> str:
        """Retrieve and return the text of an element."""
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    @property
    def _window_handles(self) -> list[str]:
        """Return a list of all open window handles."""
        return self._driver.window_handles

    def _switch_to_window(self, window_handle: str):
        """Switch the browser context to the specified window."""
        self._driver.switch_to.window(window_handle)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 5):
        """Wait until an element becomes visible on the page."""
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))
