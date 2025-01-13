from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Wrapper for selenium operations."""

    def __init__(self, driver: WebDriver):
        self._driver = driver
