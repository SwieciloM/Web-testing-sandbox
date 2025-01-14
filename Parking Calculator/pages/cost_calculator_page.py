from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CostCalculatorPage(BasePage):
    """Cost calculator page - The main and only page of the app."""

    __url = "https://www.shino.de/parkcalc/"
    __parking_type_dropdown_locator = (By.ID, "ParkingLot")
    __valet_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Valet']")
    __short_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Short']")
    __economy_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Economy']")
    __long_garage_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Long-Garage']")
    __long_surface_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Long-Surface']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def calculate_cost(self, parking_type: str, entry_date: str, entry_time: str, leaving_date: str, leaving_time: str, use_widget: bool = False):
        super()._select_from_dropdown(self.__parking_type_dropdown_locator, self.__long_surface_option_locator)

    def get_cost(self) -> float:
        pass

    def get_parking_time(self) -> int:
        pass
