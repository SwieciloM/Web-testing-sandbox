from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DatePickerPage(BasePage):
    """Date picker page for date entry via an interactive calendar"""

    __month_dropdown_locator = (By.NAME, "MonthSelector")
    __january_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(1)")
    __february_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(2)")
    __march_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(3)")
    __april_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(4)")
    __may_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(5)")
    __june_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(6)")
    __july_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(7)")
    __august_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(8)")
    __september_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(9)")
    __october_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(10)")
    __november_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(11)")
    __december_option_locator = (By.CSS_SELECTOR, "select[name='MonthSelector'] option:nth-child(12)")
    __year_increment_button_locator = (By.CSS_SELECTOR, "a[href*='IncYear']")
    __year_decrement_button_locator = (By.CSS_SELECTOR, "a[href*='DecYear']")
    __year_text_locator = (By.CSS_SELECTOR, "td[align='right'] font b")
    __day_buttons_locator = (By.CSS_SELECTOR, "a[href*='window.close']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _select_year(self, year: int):
        current_year = int(super()._get_text(self.__year_text_locator).strip())
        year_difference = year - current_year

        if year_difference > 0:
            for _ in range(year_difference):
                super()._click(self.__year_increment_button_locator)
        elif year_difference < 0:
            for _ in range(-year_difference):
                super()._click(self.__year_decrement_button_locator)

    def _select_month(self, month: int):
        super()._click(self.__month_dropdown_locator)

        month_locator = {
            1: self.__january_option_locator,
            2: self.__february_option_locator,
            3: self.__march_option_locator,
            4: self.__april_option_locator,
            5: self.__may_option_locator,
            6: self.__june_option_locator,
            7: self.__july_option_locator,
            8: self.__august_option_locator,
            9: self.__september_option_locator,
            10: self.__october_option_locator,
            11: self.__november_option_locator,
            12: self.__december_option_locator,
        }

        if month in month_locator:
            super()._click(month_locator[month])
        else:
            raise ValueError(f"Invalid month: {month}. Please provide a value between 1 and 12.")

    def _select_day(self, day: int):
        day_elements = super()._find_all(self.__day_buttons_locator)
        days_num = len(day_elements)

        if 1 <= day <= days_num:
            for day_element in day_elements:
                if int(super()._get_text(day_element).strip()) == day:
                    super()._click(day_element)
        else:
            raise ValueError(f"Invalid day: {day}. Please provide a value between 1 and {days_num}.")

    def select_date(self, text_date: str):
        self._select_year(2030)
        self._select_month(10)
        self._select_day(30)

