from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page for authentication of registered users."""

    __url = "https://bookcart.azurewebsites.net/login"
    __username_field_locator = (By.ID, "mat-input-0")
    __password_field_locator = (By.ID, "mat-input-1")
    __login_button_locator = (By.XPATH, "//button[.//span[text()='Login']]")

    def __init__(self, driver: WebDriver):
        """Initialize the login page with a WebDriver instance."""
        super().__init__(driver)

    def open(self):
        """Open the login page in the browser."""
        super()._open_url(self.__url)

    def log_in(self, username: str, password: str):
        """Fill in login credentials and submit the form."""
        super()._type(self.__username_field_locator, username)
        super()._type(self.__password_field_locator, password)
        super()._click(self.__login_button_locator)
