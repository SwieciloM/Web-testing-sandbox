<h1 align="center">PARKING CALCULATOR – TEST FINAL SUMMARY</h1>

**Report Date**: January 19, 2025  
**Author**: Michał Święciło  

### 1. Objectives
The primary objective of this testing effort was to verify the functionality of the Parking Cost Calculator, including:
- **Cost calculation logic** across various parking types (Valet, Short-Term, Economy, etc.).
- **Input validation** for time and date ranges.
- **User interface interactivity**, such as buttons, dropdowns, and date pickers.
- **Cross-browser compatibility** on Chrome, Firefox, Safari, and Edge.

### 2. Test Execution Results
**Total Test Cases executed**: 354  
**Execution Time**: 00:61:01  

| **Status**   | **Count** |
|--------------|-----------|
| Passed       | 252       |
| Failed       | 102       |
| Skipped      | 0         |
| Errors       | 0         |

### 3. Environment
- **Platform**: Windows 10 (10.0.19041-SP0)
- **Python**: 3.9.2
- **Browser Drivers**: ChromeDriver, FirefoxDriver, EdgeDriver
- **Automation Tools**: Selenium, pytest, pytest-html

### 4. Key Findings

#### 4.1 Passed Tests
- The majority of tests for **cost calculation logic** passed successfully across different parking types and scenarios.
- UI components such as dropdowns and checkboxes functioned as expected in all environments.

#### 4.2 Failed Tests
102 test cases failed, primarily due to:
- **Edge Cases**: Incorrect handling of more complicated parking times (e.g., `TC-ST-11-NDP`).
- **Error Messages**: Missing error messages for invalid inputs, as seen in `TC-VAL-01-DP` and `TC-ST-01-NDP`.

#### 4.3 Notable Defects
1. **Bug #001**: Negative parking durations do not display an error message (Test Case: `TC-VAL-01-NDP`).  
   - **Severity**: High  
   - **Recommendation**: Update validation logic.

2. **Bug #002**: Missing error messages for invalid entry and leaving times (Test Case: `TC-ST-01-DP`).  
   - **Severity**: High  
   - **Recommendation**: Ensure robust input validation.

### 5. Risks
- **Absence of test coverage for safari**: Testing on Safari was limited due to lack of required hardware 
- **Third-party hosting**: The application is externally hosted, increasing the risk of access disruptions.

### 6. Recommendations
1. **Fix Critical Defects**:
   - Address issues related to input validation and missing error messages.
3. **Enhance Test Coverage**:
   - Conduct additional tests on Safari and edge cases.
4. **Regression Testing**:
   - Re-run tests after fixing defects to ensure no new issues are introduced.
