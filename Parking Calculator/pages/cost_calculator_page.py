from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from enums.parking_type import ParkingType
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
    __starting_date_field_locator = (By.ID, "StartingDate")
    __leaving_date_field_locator = (By.ID, "LeavingDate")
    __starting_date_widget_locator = (By.XPATH, r"//a[@href=\"javascript:NewCal('StartingDate','mmddyyyy',false,24)\"]")
    __leaving_date_widget_locator = (By.XPATH, r"//a[@href=\"javascript:NewCal('LeavingDate','mmddyyyy',false,24)\"]")
    __starting_time_field_locator = (By.ID, "StartingTime")
    __leaving_time_field_locator = (By.ID, "LeavingTime")
    __submit_button_locator = (By.CSS_SELECTOR, "input[name='Submit']")
    __output_message_locator = (By.CSS_SELECTOR, "td[class='SubHead']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def calculate_cost(self, parking_type: ParkingType, entry_date: str, entry_time: str, leaving_date: str, leaving_time: str, use_widget: bool = False):
        if parking_type == ParkingType.VALET:
            super()._select_from_dropdown(self.__parking_type_dropdown_locator, self.__valet_option_locator)
        elif parking_type == ParkingType.SHORT_TERM:
            super()._select_from_dropdown(self.__parking_type_dropdown_locator, self.__short_option_locator)
        elif parking_type == ParkingType.LONG_TERM_GARAGE:
            super()._select_from_dropdown(self.__parking_type_dropdown_locator, self.__long_garage_option_locator)
        elif parking_type == ParkingType.LONG_TERM_SURFACE:
            super()._select_from_dropdown(self.__parking_type_dropdown_locator, self.__long_surface_option_locator)
        elif parking_type == ParkingType.ECONOMY:
            super()._select_from_dropdown(self.__parking_type_dropdown_locator, self.__economy_option_locator)

        if use_widget:
            super()._enter_date_via_widget()
            super()._enter_date_via_widget()
        else:
            super()._type(self.__starting_date_field_locator, entry_date)
            super()._type(self.__leaving_date_field_locator, leaving_date)

        super()._type(self.__starting_time_field_locator, entry_time)
        super()._type(self.__leaving_time_field_locator, leaving_time)

        super()._click(self.__submit_button_locator)

    def get_cost(self) -> float:
        pass

    def get_parking_time(self) -> int:
        pass
