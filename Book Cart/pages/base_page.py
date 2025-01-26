from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Union


class BasePage:
    """Wrapper for selenium operations."""

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        """
        Opens a specified URL in the browser.

        :param url: The URL to open.
        """
        self._driver.get(url)

    def _is_displayed(self, locator: tuple) -> bool:
        """
        Checks if an element is displayed on the page.

        :param locator: Locator tuple (e.g., (By.ID, "element_id")) for the element.
        :return: True if the element is displayed, False otherwise.
        """
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _find(self, locator: tuple) -> WebElement:
        """
        Finds a single web element using the provided locator.

        :param locator: Locator tuple (e.g., (By.ID, "element_id")) for the element.
        :return: The found WebElement.
        """
        return self._driver.find_element(*locator)

    def _find_all(self, locator: tuple) -> list[WebElement]:
        """
        Finds all web elements matching the provided locator.

        :param locator: Locator tuple (e.g., (By.CLASS_NAME, "elements")) for the elements.
        :return: A list of WebElements matching the locator.
        """
        return self._driver.find_elements(*locator)

    def _type(self, locator: tuple, text: str):
        """
        Types text into a field, clearing any existing content first.

        :param locator: Locator tuple (e.g., (By.NAME, "field_name")) for the input field.
        :param text: The text to type into the field.
        """
        field_element = self._find(locator)
        field_element.clear()
        field_element.send_keys(text)

    def _click(self, locator_or_element: Union[tuple, WebElement]):
        """
        Clicks on a web element, either specified by a locator or passed as a WebElement.

        :param locator_or_element: A locator tuple (e.g., (By.XPATH, "//button"))
                                   or a WebElement instance.
        :raises TypeError: If the argument is neither a locator tuple nor a WebElement.
        """
        if isinstance(locator_or_element, tuple):
            element = self._find(locator_or_element)
        elif isinstance(locator_or_element, WebElement):
            element = locator_or_element
        else:
            raise TypeError("Argument must be a locator tuple or WebElement.")
        element.click()

    def _select_from_dropdown(self, dropdown_locator: tuple, option_locator: tuple):
        """
        Selects an option from a dropdown menu by clicking on the dropdown and then the option.

        :param dropdown_locator: Locator tuple for the dropdown element.
        :param option_locator: Locator tuple for the option to select.
        """
        self._find(dropdown_locator).click()
        self._find(option_locator).click()

    def _get_text(self, locator_or_element: Union[tuple, WebElement]) -> str:
        """
        Retrieves the visible text of an element.

        :param locator_or_element: A locator tuple (e.g., (By.CSS_SELECTOR, ".class"))
                                   or a WebElement instance.
        :return: The visible text of the element.
        :raises TypeError: If the argument is neither a locator tuple nor a WebElement.
        """
        if isinstance(locator_or_element, tuple):
            element = self._find(locator_or_element)
        elif isinstance(locator_or_element, WebElement):
            element = locator_or_element
        else:
            raise TypeError("Argument must be a locator tuple or WebElement.")
        return element.text

    @property
    def _window_handles(self) -> list[str]:
        """
        Retrieves all window handles of the browser.

        :return: A list of strings representing the window handles.
        """
        return self._driver.window_handles

    def _switch_to_window(self, window_handle: str):
        """
        Switches to a specific browser window by its handle.

        :param window_handle: The handle of the window to switch to.
        """
        self._driver.switch_to.window(window_handle)