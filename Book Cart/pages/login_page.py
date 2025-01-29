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
        super().__init__(driver)

    def open(self):
        """
        Opens the login page in the browser.
        """

        super()._open_url(self.__url)

    def log_in(self, username: str, password: str):
        """
        Fills the login form and submits it.

        :param username: Username for authentication.
        :param password: Password associated with the user account.
        """
        super()._type(self.__username_field_locator, username)
        super()._type(self.__password_field_locator, password)
        super()._click(self.__login_button_locator)

