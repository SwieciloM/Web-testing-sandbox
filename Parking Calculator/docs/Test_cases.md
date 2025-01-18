<h1 align="center">PARKING CALCULATOR – TEST CASES</h1>

### 1. Valet Parking

> **Rates**:  
> - \$18 per day
> - \$12 for five hours or less 

| **Test Case ID** | **Parking Time** | **Date Picker Used** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|----------------------|-------------------|-----------------|------------|
| TC-VAL-01-NDP    | -1 min           | FALSE                | ERROR             |                 |            |
| TC-VAL-01-DP     | -1 min           | TRUE                 | ERROR             |                 |            |
| TC-VAL-02-NDP    | 0 min            | FALSE                | 0                 |                 |            |
| TC-VAL-02-DP     | 0 min            | TRUE                 | 0                 |                 |            |
| TC-VAL-03-NDP    | 1 min            | FALSE                | 12$               |                 |            |
| TC-VAL-03-DP     | 1 min            | TRUE                 | 12$               |                 |            |
| TC-VAL-04-NDP    | 5 hrs            | FALSE                | 12$               |                 |            |
| TC-VAL-04-DP     | 5 hrs            | TRUE                 | 12$               |                 |            |
| TC-VAL-05-NDP    | 5 hrs, 1 min     | FALSE                | 18$               |                 |            |
| TC-VAL-05-DP     | 5 hrs, 1 min     | TRUE                 | 18$               |                 |            |
| TC-VAL-06-NDP    | 24 hrs           | FALSE                | 18$               |                 |            |
| TC-VAL-06-DP     | 24 hrs           | TRUE                 | 18$               |                 |            |
| TC-VAL-07-NDP    | 24 hrs, 1 min    | FALSE                | 30$               |                 |            |
| TC-VAL-07-DP     | 24 hrs, 1 min    | TRUE                 | 30$               |                 |            |

---

### 2. Short-Term Parking

> **Rates**:  
> - \$2.00 first hour  
> - \$1.00 each additional 1/2 hour  
> - \$24.00 daily maximum

| **Test Case ID** | **Parking Time** | **Date Picker Used** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|----------------------|-------------------|-----------------|------------|
| TC-ST-01-NDP     | -1 min           | FALSE                | ERROR             |                 |            |
| TC-ST-01-DP      | -1 min           | TRUE                 | ERROR             |                 |            |
| TC-ST-02-NDP     | 0 min            | FALSE                | 0                 |                 |            |
| TC-ST-02-DP      | 0 min            | TRUE                 | 0                 |                 |            |
| TC-ST-03-NDP     | 1 min            | FALSE                | 2$                |                 |            |
| TC-ST-03-DP      | 1 min            | TRUE                 | 2$                |                 |            |
| TC-ST-04-NDP     | 1 hr             | FALSE                | 2$                |                 |            |
| TC-ST-04-DP      | 1 hr             | TRUE                 | 2$                |                 |            |
| TC-ST-05-NDP     | 1 hr, 1 min      | FALSE                | 3$                |                 |            |
| TC-ST-05-DP      | 1 hr, 1 min      | TRUE                 | 3$                |                 |            |
| TC-ST-06-NDP     | 1 hr, 30 min     | FALSE                | 3$                |                 |            |
| TC-ST-06-DP      | 1 hr, 30 min     | TRUE                 | 3$                |                 |            |
| TC-ST-07-NDP     | 1 hr, 31 min     | FALSE                | 4$                |                 |            |
| TC-ST-07-DP      | 1 hr, 31 min     | TRUE                 | 4$                |                 |            |
| TC-ST-08-NDP     | 12 hrs           | FALSE                | 24$               |                 |            |
| TC-ST-08-DP      | 12 hrs           | TRUE                 | 24$               |                 |            |
| TC-ST-09-NDP     | 12 hrs, 1 min    | FALSE                | 24$               |                 |            |
| TC-ST-09-DP      | 12 hrs, 1 min    | TRUE                 | 24$               |                 |            |
| TC-ST-10-NDP     | 24 hrs           | FALSE                | 24$               |                 |            |
| TC-ST-10-DP      | 24 hrs           | TRUE                 | 24$               |                 |            |
| TC-ST-11-NDP     | 24 hrs, 1 min    | FALSE                | 26$               |                 |            |
| TC-ST-11-DP      | 24 hrs, 1 min    | TRUE                 | 26$               |                 |            |

---

### 3. Long-Term Garage Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$12.00 daily maximum  
> - \$72.00 per week (7th day free)

| **Test Case ID** | **Parking Time** | **Date Picker Used** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|----------------------|-------------------|-----------------|------------|
| TC-LTG-01-NDP    | -1 min           | FALSE                | ERROR             |                 |            |
| TC-LTG-01-DP     | -1 min           | TRUE                 | ERROR             |                 |            |
| TC-LTG-02-NDP    | 0 min            | FALSE                | 0                 |                 |            |
| TC-LTG-02-DP     | 0 min            | TRUE                 | 0                 |                 |            |
| TC-LTG-03-NDP    | 1 min            | FALSE                | 2$                |                 |            |
| TC-LTG-03-DP     | 1 min            | TRUE                 | 2$                |                 |            |
| TC-LTG-04-NDP    | 1 hr             | FALSE                | 2$                |                 |            |
| TC-LTG-04-DP     | 1 hr             | TRUE                 | 2$                |                 |            |
| TC-LTG-05-NDP    | 1 hr, 1 min      | FALSE                | 4$                |                 |            |
| TC-LTG-05-DP     | 1 hr, 1 min      | TRUE                 | 4$                |                 |            |
| TC-LTG-06-NDP    | 6 hrs            | FALSE                | 12$               |                 |            |
| TC-LTG-06-DP     | 6 hrs            | TRUE                 | 12$               |                 |            |
| TC-LTG-07-NDP    | 6 hrs, 1 min     | FALSE                | 12$               |                 |            |
| TC-LTG-07-DP     | 6 hrs, 1 min     | TRUE                 | 12$               |                 |            |
| TC-LTG-08-NDP    | 24 hrs           | FALSE                | 12$               |                 |            |
| TC-LTG-08-DP     | 24 hrs           | TRUE                 | 12$               |                 |            |
| TC-LTG-09-NDP    | 24 hrs, 1 min    | FALSE                | 14$               |                 |            |
| TC-LTG-09-DP     | 24 hrs, 1 min    | TRUE                 | 14$               |                 |            |
| TC-LTG-10-NDP    | 144 hrs          | FALSE                | 72$               |                 |            |
| TC-LTG-10-DP     | 144 hrs          | TRUE                 | 72$               |                 |            |
| TC-LTG-11-NDP    | 144 hrs, 1 min   | FALSE                | 72$               |                 |            |
| TC-LTG-11-DP     | 144 hrs, 1 min   | TRUE                 | 72$               |                 |            |
| TC-LTG-12-NDP    | 168 hrs          | FALSE                | 72$               |                 |            |
| TC-LTG-12-DP     | 168 hrs          | TRUE                 | 72$               |                 |            |
| TC-LTG-13-NDP    | 168 hrs, 1 min   | FALSE                | 74$               |                 |            |
| TC-LTG-13-DP     | 168 hrs, 1 min   | TRUE                 | 74$               |                 |            |

---

### 4. Long-Term Surface Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$10.00 daily maximum  
> - \$60.00 per week (7th day free)

| **Test Case ID** | **Parking Time** | **Date Picker Used** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|----------------------|-------------------|-----------------|------------|
| TC-LTS-01-NDP    | -1 min           | FALSE                | ERROR             |                 |            |
| TC-LTS-01-DP     | -1 min           | TRUE                 | ERROR             |                 |            |
| TC-LTS-02-NDP    | 0 min            | FALSE                | 0                 |                 |            |
| TC-LTS-02-DP     | 0 min            | TRUE                 | 0                 |                 |            |
| TC-LTS-03-NDP    | 1 min            | FALSE                | 2$                |                 |            |
| TC-LTS-03-DP     | 1 min            | TRUE                 | 2$                |                 |            |
| TC-LTS-04-NDP    | 1 hr             | FALSE                | 2$                |                 |            |
| TC-LTS-04-DP     | 1 hr             | TRUE                 | 2$                |                 |            |
| TC-LTS-05-NDP    | 1 hr, 1 min      | FALSE                | 4$                |                 |            |
| TC-LTS-05-DP     | 1 hr, 1 min      | TRUE                 | 4$                |                 |            |
| TC-LTS-06-NDP    | 5 hrs            | FALSE                | 10$               |                 |            |
| TC-LTS-06-DP     | 5 hrs            | TRUE                 | 10$               |                 |            |
| TC-LTS-07-NDP    | 5 hrs, 1 min     | FALSE                | 10$               |                 |            |
| TC-LTS-07-DP     | 5 hrs, 1 min     | TRUE                 | 10$               |                 |            |
| TC-LTS-08-NDP    | 24 hrs           | FALSE                | 10$               |                 |            |
| TC-LTS-08-DP     | 24 hrs           | TRUE                 | 10$               |                 |            |
| TC-LTS-09-NDP    | 24 hrs, 1 min    | FALSE                | 12$               |                 |            |
| TC-LTS-09-DP     | 24 hrs, 1 min    | TRUE                 | 12$               |                 |            |
| TC-LTS-10-NDP    | 144 hrs          | FALSE                | 60$               |                 |            |
| TC-LTS-10-DP     | 144 hrs          | TRUE                 | 60$               |                 |            |
| TC-LTS-11-NDP    | 144 hrs, 1 min   | FALSE                | 60$               |                 |            |
| TC-LTS-11-DP     | 144 hrs, 1 min   | TRUE                 | 60$               |                 |            |
| TC-LTS-12-NDP    | 168 hrs          | FALSE                | 60$               |                 |            |
| TC-LTS-12-DP     | 168 hrs          | TRUE                 | 60$               |                 |            |
| TC-LTS-13-NDP    | 168 hrs, 1 min   | FALSE                | 62$               |                 |            |
| TC-LTS-13-DP     | 168 hrs, 1 min   | TRUE                 | 62$               |                 |            |

---

### 5. Economy Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$9.00 daily maximum  
> - \$54.00 per week (7th day free)

| **Test Case ID** | **Parking Time** | **Date Picker Used** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|----------------------|-------------------|-----------------|------------|
| TC-ECO-01-NDP    | -1 min           | FALSE                | ERROR             |                 |            |
| TC-ECO-01-DP     | -1 min           | TRUE                 | ERROR             |                 |            |
| TC-ECO-02-NDP    | 0 min            | FALSE                | 0                 |                 |            |
| TC-ECO-02-DP     | 0 min            | TRUE                 | 0                 |                 |            |
| TC-ECO-03-NDP    | 1 min            | FALSE                | 2$                |                 |            |
| TC-ECO-03-DP     | 1 min            | TRUE                 | 2$                |                 |            |
| TC-ECO-04-NDP    | 1 hr             | FALSE                | 2$                |                 |            |
| TC-ECO-04-DP     | 1 hr             | TRUE                 | 2$                |                 |            |
| TC-ECO-05-NDP    | 1 hr, 1 min      | FALSE                | 4$                |                 |            |
| TC-ECO-05-DP     | 1 hr, 1 min      | TRUE                 | 4$                |                 |            |
| TC-ECO-06-NDP    | 4 hrs            | FALSE                | 8$                |                 |            |
| TC-ECO-06-DP     | 4 hrs            | TRUE                 | 8$                |                 |            |
| TC-ECO-07-NDP    | 4 hrs, 1 min     | FALSE                | 9$                |                 |            |
| TC-ECO-07-DP     | 4 hrs, 1 min     | TRUE                 | 9$                |                 |            |
| TC-ECO-08-NDP    | 5 hrs            | FALSE                | 9$                |                 |            |
| TC-ECO-08-DP     | 5 hrs            | TRUE                 | 9$                |                 |            |
| TC-ECO-09-NDP    | 5 hrs, 1 min     | FALSE                | 9$                |                 |            |
| TC-ECO-09-DP     | 5 hrs, 1 min     | TRUE                 | 9$                |                 |            |
| TC-ECO-10-NDP    | 24 hrs           | FALSE                | 9$                |                 |            |
| TC-ECO-10-DP     | 24 hrs           | TRUE                 | 9$                |                 |            |
| TC-ECO-11-NDP    | 24 hrs, 1 min    | FALSE                | 11$               |                 |            |
| TC-ECO-11-DP     | 24 hrs, 1 min    | TRUE                 | 11$               |                 |            |
| TC-ECO-12-NDP    | 144 hrs          | FALSE                | 54$               |                 |            |
| TC-ECO-12-DP     | 144 hrs          | TRUE                 | 54$               |                 |            |
| TC-ECO-13-NDP    | 144 hrs, 1 min   | FALSE                | 54$               |                 |            |
| TC-ECO-13-DP     | 144 hrs, 1 min   | TRUE                 | 54$               |                 |            |
| TC-ECO-14-NDP    | 168 hrs          | FALSE                | 54$               |                 |            |
| TC-ECO-14-DP     | 168 hrs          | TRUE                 | 54$               |                 |            |
| TC-ECO-15-NDP    | 168 hrs, 1 min   | FALSE                | 56$               |                 |            |
| TC-ECO-15-DP     | 168 hrs, 1 min   | TRUE                 | 56$               |                 |            |

---

### Notes & Assumptions

1. **Partial Hour Billing**  
   - Short-Term parking uses increments of the first hour at \$2.00, then \$1.00 per each additional 30 minutes.
   - No partial increments beyond the stated half-hour or hourly rates.

2. **Daily and Weekly Max**  
   - After hitting the daily max, the system charges no more within that 24-hour window.  
   - After hitting the weekly max, the 7th day is free.

3. **Lost Ticket Handling**  
   - Since lost ticket functionality is not implemented, it will not be covered by tests. 
   - All test scenarios assume that the user has a valid ticket when accounting for parking fees.

4. **Test Data**    
   - As the parking time can theoretically be infinite the test cases are limited to the most critical scenarios.

---
