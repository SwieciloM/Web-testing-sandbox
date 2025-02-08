from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from enums.gender import Gender


class RegisterPage(BasePage):
    """Register page for new account creation."""

    __url = "https://bookcart.azurewebsites.net/register"
    __first_name_field_locator = (By.ID, "mat-input-0")
    __last_name_field_locator = (By.ID, "mat-input-1")
    __username_field_locator = (By.ID, "mat-input-2")
    __password_field_locator = (By.ID, "mat-input-3")
    __password_confirm_field_locator = (By.ID, "mat-input-4")
    __gender_male_checkbox_locator = (By.ID, "mat-radio-0")
    __gender_female_checkbox_locator = (By.ID, "mat-radio-1")
    __register_button_locator = (By.XPATH, "//button[.//span[text()='Register']]")

    def __init__(self, driver: WebDriver):
        """Initialize the register page with a WebDriver instance."""
        super().__init__(driver)

    def open(self):
        """Open the register page in the browser."""
        super()._open_url(self.__url)

    def register(self, first_name: str, last_name: str, gender: Gender, username: str, password: str):
        """Fill in the registration form and submit it."""
        super()._type(self.__first_name_field_locator, first_name)
        super()._type(self.__last_name_field_locator, last_name)
        super()._type(self.__username_field_locator, username)
        super()._type(self.__password_field_locator, password)
        super()._type(self.__password_confirm_field_locator, password)
        super()._click(self.__gender_male_checkbox_locator if gender == Gender.MALE else self.__gender_female_checkbox_locator)
        super()._click(self.__register_button_locator)
