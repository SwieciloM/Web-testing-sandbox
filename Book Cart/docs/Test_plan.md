<h1 align="center">BOOK CART – TEST PLAN</h1>

### 1. Introduction
This document outlines the test plan for the [BookCart](https://bookcart.azurewebsites.net/) web application, designed to simulate E-commerce bookstore. The page also includes documentation for BookCart API.

### 2. Goals
The main goal is to determine the quality of the application through tests that are designed to find as many defects as possible.

### 3. Test strategy
In order to meet the project objectives, the following tests will be conducted:
- Automated functional tests on multiple browsers (Chrome, Firefox, Safari, Edge)
- Manual functional tests necessary to obtain information for the bug reports

### 4. Scope
#### 4.1 In Scope
- Most common workflows including:
  - User authentication & authorization (registration, login, logout)
  - Product browsing & search
  - Shopping cart & checkout
- Basic API requests
- Widgets interactivity (buttons, dropdowns, checkboxes)
- System behaviour on different browsers

#### 4.2 Out of Scope
- Non-functional features (e.g. performance)
- Advanced security

### 5. Roles and Responsibilities
- **Test Lead/Tester**: Me (Michał Święciło)

### 6. Entry Criteria
- The app is deployed and accessible at [BookCart](https://bookcart.azurewebsites.net/)
- Python environment with Selenium is ready

### 7. Exit Criteria
- All planned test cases executed
- All bug reports created
- Final report created

### 8. Schedule
| **Phase**              | **Start Date** | **End Date**   | **Owner** | **Status**     |
|------------------------|----------------|----------------|-----------|----------------|
| Test Planning          | 2025-01-27     | 2025-01-31     | Me        | ✅ Completed   |
| Test Analysis & Design | 2025-02-01     | 2025-02-08     | Me        | 🔄 In Progress |
| Test Implementation    | 2025-02-03     | 2025-02-10     | Me        | 🔄 In Progress |
| Test Execution         | 2025-02-05     | 2025-02-12     | Me        | ❌ Not Started |
| Finalization           | 2025-02-07     | 2025-02-16     | Me        | ❌ Not Started |

### 9. Tools and Technologies
- Python 3.9 with selenium, pytest, pytest-html, pytest-xdis and requests libraries
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
