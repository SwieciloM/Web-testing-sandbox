<h1 align="center">PARKING CALCULATOR – TEST CASES</h1>

### 1. Valet Parking

| **Test Case ID** | **TC-VAL-01**                                                          |
|------------------|-------------------------------------------------------------------------|
| **Title**        | Verify Valet Parking Rate (5 hours or less)                             |
| **Precondition** | Customer parks in Valet Parking.                                        |
| **Steps**        | 1. Park for 5 hours or less.<br>2. Request fee upon exit.               |
| **Expected**     | Fee = **\$12** (flat rate for 5 hours or less).                         |
| **Actual**       | *To be filled after execution*                                          |
| **Status**       | *Pass / Fail / Blocked*                                                |

| **Test Case ID** | **TC-VAL-02**                                                          |
|------------------|-------------------------------------------------------------------------|
| **Title**        | Verify Valet Parking Rate (more than 5 hours)                           |
| **Precondition** | Customer parks in Valet Parking.                                        |
| **Steps**        | 1. Park for more than 5 hours.<br>2. Request fee upon exit.             |
| **Expected**     | Fee = **\$18** per day (flat daily rate).                               |
| **Actual**       | *To be filled after execution*                                          |
| **Status**       | *Pass / Fail / Blocked*                                                |

| **Test Case ID** | **TC-VAL-03**                                                     |
|------------------|--------------------------------------------------------------------|
| **Title**        | Verify Lost Ticket Fee does NOT apply to Valet Parking            |
| **Precondition** | Customer used Valet Parking and lost the ticket.                  |
| **Steps**        | 1. Park in Valet.<br>2. Lose the ticket stub.<br>3. Request fee.  |
| **Expected**     | **No extra** \$10 lost ticket fee for Valet. Fee remains \$18/day or \$12 if ≤ 5 hrs. |
| **Actual**       | *To be filled after execution*                                     |
| **Status**       | *Pass / Fail / Blocked*                                           |

---

### 2. Short-Term (Hourly) Parking

> **Rates**:  
> - \$2.00 first hour  
> - \$1.00 each additional 1/2 hour  
> - \$24.00 daily maximum

| **Test Case ID** | **TC-SH-01**                                                                        |
|------------------|--------------------------------------------------------------------------------------|
| **Title**        | Verify Rate for 1 Hour in Short-Term Parking                                        |
| **Precondition** | Customer parks in Short-Term lot.                                                   |
| **Steps**        | 1. Park for exactly 1 hour.<br>2. Request fee.                                      |
| **Expected**     | Fee = **\$2.00**.                                                                    |
| **Actual**       | *To be filled after execution*                                                       |
| **Status**       | *Pass / Fail / Blocked*                                                             |

| **Test Case ID** | **TC-SH-02**                                                                        |
|------------------|--------------------------------------------------------------------------------------|
| **Title**        | Verify Rate for 2 Hours in Short-Term Parking                                       |
| **Precondition** | Customer parks in Short-Term lot.                                                   |
| **Steps**        | 1. Park for exactly 2 hours.<br>2. Request fee. <br> - 1 hour = \$2.00 <br> - Next 1 hour = 2 half-hours × \$1.00 each |
| **Expected**     | Fee = **\$4.00** ( \$2.00 + \$1.00 + \$1.00 ).                                       |
| **Actual**       | *To be filled after execution*                                                       |
| **Status**       | *Pass / Fail / Blocked*                                                             |

| **Test Case ID** | **TC-SH-03**                                                                       |
|------------------|-------------------------------------------------------------------------------------|
| **Title**        | Verify Daily Maximum in Short-Term Parking                                          |
| **Precondition** | Customer parks in Short-Term lot.                                                   |
| **Steps**        | 1. Park for more than 12 hours (or enough to exceed \$24).<br>2. Request fee.       |
| **Expected**     | Fee = **\$24.00** (daily max).                                                      |
| **Actual**       | *To be filled after execution*                                                      |
| **Status**       | *Pass / Fail / Blocked*                                                            |

| **Test Case ID** | **TC-SH-04**                                                                   |
|------------------|---------------------------------------------------------------------------------|
| **Title**        | Verify Lost Ticket Fee in Short-Term Parking                                    |
| **Precondition** | Customer parks in Short-Term lot and loses the ticket.                          |
| **Steps**        | 1. Park for any duration.<br>2. Lose the ticket.<br>3. Request fee upon exit.   |
| **Expected**     | Fee = **Parking Rate** + **\$10** Lost Ticket Fee.<br><br>*(Not applicable to Valet.)* |
| **Actual**       | *To be filled after execution*                                                  |
| **Status**       | *Pass / Fail / Blocked*                                                        |

---

### 3. Long-Term Garage Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$12.00 daily maximum  
> - \$72.00 per week (7th day free)

| **Test Case ID** | **TC-LTG-01**                                                              |
|------------------|----------------------------------------------------------------------------|
| **Title**        | Verify Hourly Rate in Long-Term Garage for Partial Day                     |
| **Precondition** | Customer parks in Long-Term Garage.                                        |
| **Steps**        | 1. Park for `X` hours (fewer than needed to hit \$12 max).<br>2. Request fee. |
| **Expected**     | Fee = **\$2.00 × X** (does not exceed \$12 daily max).                     |
| **Actual**       | *To be filled after execution*                                             |
| **Status**       | *Pass / Fail / Blocked*                                                   |

| **Test Case ID** | **TC-LTG-02**                                                          |
|------------------|------------------------------------------------------------------------|
| **Title**        | Verify Daily Maximum in Long-Term Garage                               |
| **Precondition** | Customer parks in Long-Term Garage.                                    |
| **Steps**        | 1. Park for enough hours to exceed \$12 if charged hourly.<br>2. Request fee. |
| **Expected**     | Fee = **\$12** (daily max).                                            |
| **Actual**       | *To be filled after execution*                                         |
| **Status**       | *Pass / Fail / Blocked*                                               |

| **Test Case ID** | **TC-LTG-03**                                                                     |
|------------------|-----------------------------------------------------------------------------------|
| **Title**        | Verify Weekly Rate in Long-Term Garage (7th day free)                             |
| **Precondition** | Customer parks in Long-Term Garage for 7 days.                                    |
| **Steps**        | 1. Park continuously for 7 days.<br>2. Request fee.                               |
| **Expected**     | Fee = **\$72** total for the 7-day period.                                        |
| **Actual**       | *To be filled after execution*                                                   |
| **Status**       | *Pass / Fail / Blocked*                                                          |

| **Test Case ID** | **TC-LTG-04**                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------|
| **Title**        | Verify Lost Ticket Fee in Long-Term Garage                                                   |
| **Precondition** | Customer parks in Long-Term Garage and loses the ticket.                                     |
| **Steps**        | 1. Park any duration.<br>2. Lose the ticket.<br>3. Request fee.                               |
| **Expected**     | Fee = **(Calculated Parking Rate)** + **\$10** lost ticket fee.                               |
| **Actual**       | *To be filled after execution*                                                               |
| **Status**       | *Pass / Fail / Blocked*                                                                      |

---

### 4. Long-Term Surface Parking (North Lot)

> **Rates**:  
> - \$2.00 per hour  
> - \$10.00 daily maximum  
> - \$60.00 per week (7th day free)

| **Test Case ID** | **TC-LTS-01**                                                             |
|------------------|---------------------------------------------------------------------------|
| **Title**        | Verify Daily Maximum in Long-Term Surface (North Lot)                     |
| **Precondition** | Customer parks in Long-Term Surface lot.                                  |
| **Steps**        | 1. Park until costs would exceed \$10/day.<br>2. Request fee.             |
| **Expected**     | Fee = **\$10** (daily max).                                               |
| **Actual**       | *To be filled after execution*                                            |
| **Status**       | *Pass / Fail / Blocked*                                                  |

| **Test Case ID** | **TC-LTS-02**                                                                     |
|------------------|-----------------------------------------------------------------------------------|
| **Title**        | Verify Weekly Rate in Long-Term Surface (North Lot)                               |
| **Precondition** | Customer parks in Long-Term Surface (North Lot) for 7 days.                       |
| **Steps**        | 1. Park continuously for 7 days.<br>2. Request fee.                               |
| **Expected**     | Fee = **\$60** for the 7-day period (includes the 7th day free).                  |
| **Actual**       | *To be filled after execution*                                                   |
| **Status**       | *Pass / Fail / Blocked*                                                          |

| **Test Case ID** | **TC-LTS-03**                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------|
| **Title**        | Verify Lost Ticket Fee in Long-Term Surface (North Lot)                                                 |
| **Precondition** | Customer parks in North Lot and loses the ticket.                                                       |
| **Steps**        | 1. Park any duration.<br>2. Lose the ticket.<br>3. Request fee.                                         |
| **Expected**     | Fee = **(Hourly or Daily/Weekly Rate)** + **\$10** lost ticket fee.                                     |
| **Actual**       | *To be filled after execution*                                                                          |
| **Status**       | *Pass / Fail / Blocked*                                                                                 |

---

### 5. Economy Lot Parking

> **Rates**:  
> - \$2.00 per hour  
> - \$9.00 daily maximum  
> - \$54.00 per week (7th day free)

| **Test Case ID** | **TC-ECO-01**                                                         |
|------------------|------------------------------------------------------------------------|
| **Title**        | Verify Daily Maximum in Economy Lot Parking                            |
| **Precondition** | Customer parks in Economy Lot.                                         |
| **Steps**        | 1. Park until costs would exceed \$9/day.<br>2. Request fee.           |
| **Expected**     | Fee = **\$9** (daily max).                                             |
| **Actual**       | *To be filled after execution*                                         |
| **Status**       | *Pass / Fail / Blocked*                                               |

| **Test Case ID** | **TC-ECO-02**                                                                   |
|------------------|---------------------------------------------------------------------------------|
| **Title**        | Verify Weekly Rate in Economy Lot (7th day free)                                |
| **Precondition** | Customer parks in Economy Lot for 7 days.                                       |
| **Steps**        | 1. Park continuously for 7 days.<br>2. Request fee.                             |
| **Expected**     | Fee = **\$54** total for the 7-day period.                                      |
| **Actual**       | *To be filled after execution*                                                  |
| **Status**       | *Pass / Fail / Blocked*                                                        |

| **Test Case ID** | **TC-ECO-03**                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------|
| **Title**        | Verify Lost Ticket Fee in Economy Lot                                                        |
| **Precondition** | Customer parks in Economy Lot and loses the ticket.                                          |
| **Steps**        | 1. Park any duration.<br>2. Lose ticket.<br>3. Request fee.                                  |
| **Expected**     | Fee = **(Hourly or Daily/Weekly Rate)** + **\$10** lost ticket fee.                          |
| **Actual**       | *To be filled after execution*                                                               |
| **Status**       | *Pass / Fail / Blocked*                                                                      |

---

### 6. Global Lost Ticket Fee Validation

| **Test Case ID** | **TC-LOST-01**                                                                                   |
|------------------|--------------------------------------------------------------------------------------------------|
| **Title**        | Verify Lost Ticket Fee Applies to Non-Valet Parking                                              |
| **Precondition** | Customer parks in any lot **except** Valet and loses the ticket.                                 |
| **Steps**        | 1. Park any duration.<br>2. Lose ticket.<br>3. Attempt to pay upon exit without the ticket stub. |
| **Expected**     | Fee = **(Applicable Rate)** + **\$10** Lost Ticket Fee.                                          |
| **Actual**       | *To be filled after execution*                                                                   |
| **Status**       | *Pass / Fail / Blocked*                                                                          |

---

### Notes & Assumptions

1. **Partial Hour Billing**  
   - Short-Term parking uses increments of the first hour at \$2.00, then \$1.00 per each additional 30 minutes.

2. **Daily and Weekly Max**  
   - After hitting the daily max, the system charges no more within that 24-hour window.  
   - After hitting the weekly max, the 7th day is free.

3. **Lost Ticket Handling**  
   - Applies a \$10 fee to non-Valet parking.  
   - For Valet Parking, the lost ticket fee **does not apply**.

4. **Rounding**  
   - No partial increments beyond the stated half-hour or hourly rates.

5. **Test Data**  
   - Use various hours (e.g., 1h, 1.5h, 2h, 24h, 168h for 7 days) to confirm daily/weekly maximum rates.  
   - Test lost ticket scenarios for each parking option (except Valet).

---

## Summary

The above test cases verify:
- **Valet Parking**: \$12 if parked ≤ 5 hours, \$18 if > 5 hours, and no lost ticket fee.  
- **Short-Term Parking**: \$2 for the first hour, \$1 per additional 30 min, up to \$24 daily.  
- **Long-Term Garage**: \$2/hour, \$12 daily max, \$72 weekly (7th day free).  
- **Long-Term Surface (North Lot)**: \$2/hour, \$10 daily max, \$60 weekly (7th day free).  
- **Economy Lot**: \$2/hour, \$9 daily max, \$54 weekly (7th day free).  
- **Lost Ticket**: \$10 fee applies to all non-Valet lots.

