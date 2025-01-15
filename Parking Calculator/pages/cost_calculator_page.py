from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from typing import Optional

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
    __output_cost_message_locator = (By.CSS_SELECTOR, "span[class='SubHead'] b")
    __output_time_message_locator = (By.CSS_SELECTOR, "span[class='BodyCopy'] b")
    __output_error_message_locator = (By.CSS_SELECTOR, "td[class='SubHead'] b")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def calculate(self, parking_type: ParkingType, entry_date: str, entry_time: str, leaving_date: str, leaving_time: str, use_widget: bool = False):
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

    @property
    def parking_cost(self) -> Optional[float]:
        try:
            output_text = super()._get_text(self.__output_cost_message_locator)
            return float(output_text[2:].strip())
        except NoSuchElementException:
            return None

    @property
    def parking_time(self) -> Optional[int]:
        minutes_per_unit = {
            'Days': 1440,
            'Hours': 60,
            'Minutes': 1
        }

        try:
            raw_text = super()._get_text(self.__output_time_message_locator).strip()
            time_segments = raw_text.strip("()").split(", ")
            total_minutes = 0
            print(time_segments)
            for segment in time_segments:
                value, unit = segment.split(" ")
                total_minutes += int(value) * minutes_per_unit[unit]

            return total_minutes

        except NoSuchElementException:
            return None

    @property
    def error_message(self) -> Optional[str]:
        try:
            return super()._get_text(self.__output_error_message_locator).strip()
        except NoSuchElementException:
            return None
