<h1 align="center">PARKING CALCULATOR – TEST PLAN</h1>

### 1. Introduction
This document outlines the test plan for the [Parking Cost Calculator](https://www.shino.de/parkcalc/) web application, designed to calculate parking costs based on user input. The page also includes business requirements listed under the heading "Parking Rates", which serve as the test basis for designing test cases.

### 2. Goals
The main goal is to determine the quality of the application through tests that are designed to find as many defects as possible.

### 3. Test strategy
In order to meet the project objectives, the following tests will be conducted:
- Automated functional tests on multiple browsers (Chrome, Firefox, Safari, Edge)
- Manual functional tests necessary to obtain information for the bug reports

### 4. Scope
#### 4.1 In Scope
- Cost calculation logic including:
  - Different parking types (Valet, Short-Term, Economy)
  - Different date/time (with edge cases)
- Input validation
- Widgets interactivity (buttons, dropdowns, checkboxes, date picker)
- System behaviour on different browsers

#### 4.2 Out of Scope
- Non-functional features (e.g. performance)

### 5. Roles and Responsibilities
- **Test Lead/Tester**: Me (Michał Święciło)

### 6. Entry Criteria
- The app is deployed and accessible at [https://www.shino.de/parkcalc/](https://www.shino.de/parkcalc/)
- Python environment with Selenium is ready

### 7. Exit Criteria
- All planned test cases executed
- All bug reports created
- Final report created

### 8. Schedule
| **Phase**              | **Start Date** | **End Date**   | **Owner** | **Status**     |
|------------------------|----------------|----------------|-----------|----------------|
| Test Planning          | 2025-01-12     | 2025-01-13     | Me        | ✅ Completed   |
| Test Analysis & Design | 2025-01-13     | 2025-01-14     | Me        | ✅ Completed   |
| Test Implementation    | 2025-01-14     | 2025-01-16     | Me        | ✅ Completed   |
| Test Execution         | 2025-01-17     | 2025-01-18     | Me        | 🔄 In Progress |
| Finalization           | 2025-01-18     | 2025-01-19     | Me        | ❌ Not Started |

### 9. Tools and Technologies
- Python 3.9 with selenium, pytest and pytest-html libraries
- ChromeDriver, FirefoxDriver, EdgeDriver, SafariDriver

### 10. Environment
- Windows 10 with the latest browsers installed

### 11. Deliverables
- Test plan
- Test cases
- Test scripts
- Execution reports
- Bug reports
- Final summary

### 12. Risks
- Limited time for thorough testing
- Potential scope changes
- Potential loss of access to the test object (since it is externally hosted)
