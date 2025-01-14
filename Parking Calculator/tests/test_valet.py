import pytest

from pages.cost_calculator_page import CostCalculatorPage


class TestValetParking:

    @pytest.mark.valet
    @pytest.mark.valid_data
    def test_valid_data_entry(self, driver):
        login_page = CostCalculatorPage(driver)
        login_page.open()

    @pytest.mark.valet
    @pytest.mark.invalid_data
    def test_invalid_data_entry(self, driver):
        login_page = CostCalculatorPage(driver)
        login_page.open()

