# Parking Cost Calculator Testing Project

This project focuses on testing the functionality of the **Parking Cost Calculator**, a web application designed to compute parking costs based on user inputs. The testing effort aims to ensure robust cost calculation logic, accurate input validation, and seamless user experience across browsers.

## Features Tested
- **Parking Types:** Valet, Short-Term, Economy, Long-Term Garage, Long-Term Surface.
- **Cost Calculation Logic:** Daily and hourly rates, edge cases, and maximum charge thresholds.
- **Input Validation:** Handling invalid time and date ranges.
- **UI Interactivity:** Dropdowns, date pickers, buttons.
- **Cross-Browser Compatibility:** Chrome, Firefox, Edge, Safari.

## Key Findings
- **Passed Tests:** 252/354, including accurate calculations and functional UI components.
- **Failed Tests:** 102, due to edge cases and missing error messages.
- **Critical Bugs:**
  1. Missing error message for negative parking durations.
  2. Incorrect handling of overlapping time entries.

## Project Setup
To replicate the testing process, follow these steps:

### Prerequisites
1. **Environment**: Windows 10 or higher.
2. **Python**: Version 3.9 or later.
3. **Tools**: Selenium, pytest, pytest-html.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure browser drivers (e.g., ChromeDriver) are accessible from your system path.

### Running Tests
1. Execute all test cases:
   ```bash
   pytest --html=report.html
   ```
2. View test results in the generated `report.html` file.

### Links
- **Test Object**: [Parking Cost Calculator](https://www.shino.de/parkcalc/)

## Deliverables
- [Test Plan](docs/Test_plan.md)
- [Test Cases](docs/Test_cases.md)
- [Automation Scripts](tests)
- [Execution Reports](reports)
- [Specific Bug Reports](reports/individual%20bug%20reports)
