from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage


class TestAccountAccess:
    """
    Test class containing test methods for log-in and registration scenarios.
    """

    def test_login(self, driver: WebDriver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.log_in("MichalS", "StrongPassword123")




