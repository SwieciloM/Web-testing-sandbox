from selenium.webdriver.remote.webdriver import WebDriver

from enums.gender import Gender
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestAccountFunctionality:
    """
    Test class containing test methods for log-in and registration scenarios.
    """

    # def test_login(self, driver: WebDriver):
    #     login_page = LoginPage(driver)
    #     login_page.open()
    #     login_page.log_in("MichalS", "StrongPassword123")

    def test_register(self, driver: WebDriver):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.register("Daniel", "Sokolik", Gender.MALE, "DanielS", "DanielS1$")




