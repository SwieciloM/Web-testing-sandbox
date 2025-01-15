import pytest

from pages.cost_calculator_page import CostCalculatorPage
from enums.parking_type import ParkingType


class TestValetParking:

    @pytest.mark.valet
    @pytest.mark.valid_data
    def test_valid_data_entry(self, driver):
        page = CostCalculatorPage(driver)
        page.open()
        page.calculate(ParkingType.ECONOMY, "1/10/2025", "7:00", "1/15/2025", "11:00")
        cost = page.parking_cost
        print(f"Calculated cost = {cost}")
        time = page.parking_time
        print(f"Calculated time = {time}")
        error = page.error_message
        print(f"Error_message = {error}")


    # @pytest.mark.valet
    # @pytest.mark.invalid_data
    # def test_invalid_data_entry(self, driver):
    #     login_page = CostCalculatorPage(driver)
    #     login_page.open()

