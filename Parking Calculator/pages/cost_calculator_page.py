from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class CostCalculatorPage(BasePage):
    """Cost calculator page - The main and only page of the app."""

    __url = "https://www.shino.de/parkcalc/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def calculate_cost(self, parking_type: str, entry_date: str, entry_time: str, leaving_date: str, leaving_time: str):
        pass

    def get_cost(self) -> float:
        pass

    def get_parking_time(self) -> int:
        pass
