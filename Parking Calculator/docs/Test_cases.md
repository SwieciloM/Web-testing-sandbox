<h1 align="center">PARKING CALCULATOR – TEST CASES</h1>

### 1. Valet Parking

> **Rates**:  
> - \$18 per day
> - \$12 for five hours or less 

| **Test Case ID** | **Parking Time** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|-------------------|-----------------|------------|
| TC-VAL-01        | -1 min           | ERROR             |                 |            |
| TC-VAL-02        | 0 min            | 0                 |                 |            |
| TC-VAL-03        | 1 min            | 12$               |                 |            |
| TC-VAL-04        | 5 hrs            | 12$               |                 |            |
| TC-VAL-05        | 5 hrs, 1 min     | 18$               |                 |            |
| TC-VAL-06        | 24 hrs           | 18$               |                 |            |
| TC-VAL-07        | 24 hrs, 1 min    | 30$               |                 |            |

---

### 2. Short-Term Parking

> **Rates**:  
> - \$2.00 first hour  
> - \$1.00 each additional 1/2 hour  
> - \$24.00 daily maximum

| **Test Case ID** | **Parking Time** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|-------------------|-----------------|------------|
| TC-ST-01         | -1 min           | ERROR             |                 |            |
| TC-ST-02         | 0 min            | 0                 |                 |            |
| TC-ST-03         | 1 min            | 2$                |                 |            |
| TC-ST-04         | 1 hr             | 2$                |                 |            |
| TC-ST-05         | 1 hr, 1 min      | 3$                |                 |            |
| TC-ST-06         | 1 hr, 30 min     | 3$                |                 |            |
| TC-ST-07         | 1 hr, 31 min     | 4$                |                 |            |
| TC-ST-08         | 12 hrs           | 24$               |                 |            |
| TC-ST-09         | 12 hrs, 1 min    | 24$               |                 |            |
| TC-ST-10         | 24 hrs           | 24$               |                 |            |
| TC-ST-11         | 24 hrs, 1 min    | 26$               |                 |            |

---

### 3. Long-Term Garage Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$12.00 daily maximum  
> - \$72.00 per week (7th day free)

| **Test Case ID** | **Parking Time** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|-------------------|-----------------|------------|
| TC-LTG-01        | -1 min           | ERROR             |                 |            |
| TC-LTG-02        | 0 min            | 0                 |                 |            |
| TC-LTG-03        | 1 min            | 2$                |                 |            |
| TC-LTG-04        | 1 hr             | 2$                |                 |            |
| TC-LTG-05        | 1 hr, 1 min      | 4$                |                 |            |
| TC-LTG-06        | 6 hrs            | 12$               |                 |            |
| TC-LTG-07        | 6 hrs, 1 min     | 12$               |                 |            |
| TC-LTG-08        | 24 hrs           | 12$               |                 |            |
| TC-LTG-09        | 24 hrs, 1 min    | 14$               |                 |            |
| TC-LTG-10        | 144 hrs          | 72$               |                 |            |
| TC-LTG-11        | 144 hrs, 1 min   | 72$               |                 |            |
| TC-LTG-12        | 168 hrs          | 72$               |                 |            |
| TC-LTG-13        | 168 hrs, 1 min   | 74$               |                 |            |

---

### 4. Long-Term Surface Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$10.00 daily maximum  
> - \$60.00 per week (7th day free)

| **Test Case ID** | **Parking Time** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|-------------------|-----------------|------------|
| TC-LTS-01        | -1 min           | ERROR             |                 |            |
| TC-LTS-02        | 0 min            | 0                 |                 |            |
| TC-LTS-03        | 1 min            | 2$                |                 |            |
| TC-LTS-04        | 1 hr             | 2$                |                 |            |
| TC-LTS-05        | 1 hr, 1 min      | 4$                |                 |            |
| TC-LTS-06        | 5 hrs            | 10$               |                 |            |
| TC-LTS-07        | 5 hrs, 1 min     | 10$               |                 |            |
| TC-LTS-08        | 24 hrs           | 10$               |                 |            |
| TC-LTS-09        | 24 hrs, 1 min    | 12$               |                 |            |
| TC-LTS-10        | 144 hrs          | 60$               |                 |            |
| TC-LTS-11        | 144 hrs, 1 min   | 60$               |                 |            |
| TC-LTS-12        | 168 hrs          | 60$               |                 |            |
| TC-LTS-13        | 168 hrs, 1 min   | 62$               |                 |            |

---

### 5. Economy Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$9.00 daily maximum  
> - \$54.00 per week (7th day free)

| **Test Case ID** | **Parking Time** | **Expected Cost** | **Actual Cost** | **Status** |
|------------------|------------------|-------------------|-----------------|------------|
| TC-ECO-01        | -1 min           | ERROR             |                 |            |
| TC-ECO-02        | 0 min            | 0                 |                 |            |
| TC-ECO-03        | 1 min            | 2$                |                 |            |
| TC-ECO-04        | 1 hr             | 2$                |                 |            |
| TC-ECO-05        | 1 hr, 1 min      | 4$                |                 |            |
| TC-ECO-06        | 4 hrs            | 8$                |                 |            |
| TC-ECO-07        | 4 hrs, 1 min     | 9$                |                 |            |
| TC-ECO-08        | 5 hrs            | 9$                |                 |            |
| TC-ECO-09        | 5 hrs, 1 min     | 9$                |                 |            |
| TC-ECO-10        | 24 hrs           | 9$                |                 |            |
| TC-ECO-11        | 24 hrs, 1 min    | 11$               |                 |            |
| TC-ECO-12        | 144 hrs          | 54$               |                 |            |
| TC-ECO-13        | 144 hrs, 1 min   | 54$               |                 |            |
| TC-ECO-14        | 168 hrs          | 54$               |                 |            |
| TC-ECO-15        | 168 hrs, 1 min   | 56$               |                 |            |

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
