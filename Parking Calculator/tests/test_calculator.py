import pytest
import json
import os
from typing import Any

from pages.cost_calculator_page import CostCalculatorPage
from enums.parking_type import ParkingType
from selenium.webdriver.remote.webdriver import WebDriver

# A dictionary mapping each ParkingType enum member to a pytest marker
PARKING_MARKERS = {
    ParkingType.VALET: pytest.mark.valet,
    ParkingType.SHORT_TERM: pytest.mark.short_term,
    ParkingType.LONG_TERM_GARAGE: pytest.mark.long_term_garage,
    ParkingType.LONG_TERM_SURFACE: pytest.mark.long_term_surface,
    ParkingType.ECONOMY: pytest.mark.economy,
}


def load_parking_data():
    """
    Reads all parking scenarios from a json file.

    :return: A list of scenario dictionaries.
    """
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "data.json")

    with open(file_path, "r") as f:
        return json.load(f)


# List of parameters to feed into pytest.mark.parametrize
param_list = []

# Loop over every loaded scenario
for i, scenario in enumerate(load_parking_data()):
    ptype_str = scenario["parking_type"]
    marker = PARKING_MARKERS.get(ParkingType(ptype_str), None)
    test_id = scenario.get("test_case_id", i)

    # Append a new pytest.param to 'param_list', attaching the found marker if any
    if marker:
        param_list.append(pytest.param(scenario, marks=marker, id=test_id))
    else:
        param_list.append(pytest.param(scenario, id=test_id))


class TestCalculator:
    """
    Test class containing single test method that covers all parking scenarios using a single data-driven approach.
    """

    @pytest.mark.parametrize("test_data", param_list)
    def test_time_and_cost_calculation(self, driver: WebDriver, test_data: dict[str, Any]):
        """
        Verifies that the cost and time calculations displayed by the CostCalculatorPage
        match the expected values defined in each scenario.

        :param driver: The WebDriver instance provided by the 'driver' fixture.
        :param test_data: A dictionary representing one scenario from 'data.json'.
                          Must include 'parking_type', 'entry_date', 'entry_time',
                          'leaving_date', 'leaving_time', 'use_picker',
                          'expected_cost', 'parking_time_minutes', and optionally
                          'test_case_id'.
        """
        # Create a page object and open the cost calculator page
        page = CostCalculatorPage(driver)
        page.open()

        # Calculate the cost/time based on the scenario data
        page.calculate(
            parking_type=ParkingType(test_data["parking_type"]),
            entry_date=test_data["entry_date"],
            entry_time=test_data["entry_time"],
            leaving_date=test_data["leaving_date"],
            leaving_time=test_data["leaving_time"],
            use_picker=test_data["use_picker"],
        )

        # If no cost is expected, an error message should be present
        if test_data["expected_cost"] is None:
            assert page.error_message is not None, (
                f"Expected an error message for test case '{test_data.get('test_case_id')}', "
                "but none was displayed."
            )
        else:
            # Otherwise, confirm the page displays the correct cost and time
            assert page.parking_cost == test_data["expected_cost"], (
                f"Cost mismatch for test case '{test_data.get('test_case_id')}': "
                f"Expected {test_data['expected_cost']}, got {page.parking_cost}."
            )
            assert page.parking_time == test_data["parking_time_minutes"], (
                f"Time mismatch for test case '{test_data.get('test_case_id')}': "
                f"Expected {test_data['parking_time_minutes']}, got {page.parking_time}."
            )