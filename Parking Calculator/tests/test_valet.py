import pytest

from pages.cost_calculator_page import CostCalculatorPage
from enums.parking_type import ParkingType

class TestValetParking:

    @pytest.mark.valet
    @pytest.mark.valid_data
    def test_valid_data_entry(self, driver):
        login_page = CostCalculatorPage(driver)
        login_page.open()
        login_page.calculate_cost(ParkingType.ECONOMY, "1/15/2025", "7:00", "1/16/2025", "10:00")


    # @pytest.mark.valet
    # @pytest.mark.invalid_data
    # def test_invalid_data_entry(self, driver):
    #     login_page = CostCalculatorPage(driver)
    #     login_page.open()

