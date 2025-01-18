from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException
from typing import Optional

from enums.parking_type import ParkingType
from pages.date_picker_page import DatePickerPage
from pages.base_page import BasePage


class CostCalculatorPage(BasePage):
    """Cost calculator page - the main page of the app."""

    __url = "https://www.shino.de/parkcalc/"
    __parking_type_dropdown_locator = (By.ID, "ParkingLot")
    __valet_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Valet']")
    __short_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Short']")
    __economy_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Economy']")
    __long_garage_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Long-Garage']")
    __long_surface_option_locator = (By.CSS_SELECTOR, "#ParkingLot option[value='Long-Surface']")
    __starting_date_field_locator = (By.ID, "StartingDate")
    __leaving_date_field_locator = (By.ID, "LeavingDate")
    __starting_date_picker_locator = (By.CSS_SELECTOR, "a[href*='StartingDate']")
    __leaving_date_picker_locator = (By.CSS_SELECTOR, "a[href*='LeavingDate']")
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

    def _get_date_picker(self, locator: tuple) -> DatePickerPage:
        """Opens the date picker widget and switches to the new window."""
        # Get the current number of windows
        self._initial_window_count = len(self._driver.window_handles)

        super()._click(locator)

        # Wait for the new window and switch to it
        # Wait for the new window to open
        WebDriverWait(self._driver, 3).until(
            lambda driver: len(driver.window_handles) == self._initial_window_count + 1
        )

        # Switch to the new window (the last handle in the list)
        self._driver.switch_to.window(self._driver.window_handles[-1])

        return DatePickerPage(self._driver)

    def _enter_date_via_picker(self, locator: tuple, text_date: str):
        original_windows = self._driver.window_handles
        date_picker = self._get_date_picker(locator)
        try:
            date_picker.select_date(text_date)
        except:
            self._driver.switch_to.window(self._driver.window_handles[0])
            print("To zdzadziała")
        print("tutaj??????????")
        # Wait until the window count returns to 1 (original window only)
        # Wait for the number of windows to decrease
        # WebDriverWait(self._driver, 3).until(
        #     lambda driver: len(driver.window_handles) < len(original_windows)
        # )
        print("To jednak tutaj")
        # Switch to a remaining window
        # if len(self._driver.window_handles) > 0:
        #     self._driver.switch_to.window(self._driver.window_handles[0])
        # else:
        #     raise RuntimeError("All browser windows were closed unexpectedly.")

    def calculate(self, parking_type: ParkingType, entry_date: str, entry_time: str, leaving_date: str,
                  leaving_time: str, use_picker: bool = False):
        parking_type_locator = {
            ParkingType.VALET: self.__valet_option_locator,
            ParkingType.SHORT_TERM: self.__short_option_locator,
            ParkingType.LONG_TERM_GARAGE: self.__long_garage_option_locator,
            ParkingType.LONG_TERM_SURFACE: self.__long_surface_option_locator,
            ParkingType.ECONOMY: self.__economy_option_locator,
        }

        if parking_type in parking_type_locator:
            super()._select_from_dropdown(self.__parking_type_dropdown_locator, parking_type_locator[parking_type])
        else:
            raise ValueError(f"Invalid parking type: {parking_type}")

        if use_picker:
            self._enter_date_via_picker(self.__starting_date_picker_locator, entry_date)
            self._enter_date_via_picker(self.__leaving_date_picker_locator, leaving_date)
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
