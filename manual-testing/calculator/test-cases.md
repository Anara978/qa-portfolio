# Scientific Calculator — Manual Test Cases

These reproducible test cases are documented from the existing manual investigation and [Bug Report 01](bug-report-01.md). The expected and actual results below are supported by that report and its screenshots. This file organizes existing evidence; it does **not** claim the cases were originally written before the observations.

**Application:** Scientific Calculator (`index.html`)  
**Browser:** Google Chrome (version was not recorded)  
**Test type:** Manual functional / responsive UI testing  
**Execution evidence:** [Bug Report 01](bug-report-01.md)

## TC-CALC-001 — Button 7 at 400 × 740 px

| Field | Details |
| --- | --- |
| Preconditions | Calculator is open in Google Chrome; viewport set to 400 × 740 px |
| Steps | 1. Open the calculator. 2. Set viewport to 400 × 740 px. 3. Click button **7**. |
| Expected result | Button responds and the digit **7** is displayed. |
| Observed result | Button **7** does not respond. |
| Result | **Fail — observed during manual testing** |
| Evidence | [Screenshot](screenshots/viewport-400x740.webp) |

## TC-CALC-002 — Button 8 at 600 × 700 px

| Field | Details |
| --- | --- |
| Preconditions | Calculator is open in Google Chrome; viewport set to 600 × 700 px |
| Steps | 1. Open the calculator. 2. Set viewport to 600 × 700 px. 3. Click button **8**. |
| Expected result | Button responds and the digit **8** is displayed. |
| Observed result | Button **8** does not respond. |
| Result | **Fail — observed during manual testing** |
| Evidence | [Screenshot](screenshots/viewport-600x700.webp) |

## Investigation and limitations

Chrome DevTools inspection found an invisible, absolutely positioned 150 × 150 px `div` overlapping the affected button area. Safari Web Inspector was also used to inspect the layout; **reproduction of the click defect in Safari was not documented**. Browser version was not recorded. No post-fix retest is claimed. See the [bug report](bug-report-01.md) for details.
