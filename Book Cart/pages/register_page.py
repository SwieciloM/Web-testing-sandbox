from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Register page for new accounts creation."""

    __url = "https://bookcart.azurewebsites.net/register"
    __first_name_field_locator = ()
    __last_name_field_locator = ()
    __username_field_locator = ()
    __password_field_locator = ()
    __password_confirm_field_locator = ()
    __gender_male_checkbox_locator = ()
    __gender_female_checkbox_locator = ()
    __register_button_locator = ()

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        """
        Opens the register page in the browser.
        """

        super()._open_url(self.__url)

    def register(self, first_name: str, last_name: str, gender: str, username: str, password: str):
        """

        """
        super()._type(self.__first_name_field_locator, first_name)
        super()._type(self.__last_name_field_locator, last_name)
        super()._type(self.__username_field_locator, username)
        super()._type(self.__password_field_locator, password)
        super()._type(self.__gender_female_checkbox_locator, gender)
        super()._click(self.__register_button_locator)

