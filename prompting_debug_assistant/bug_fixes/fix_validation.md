# Code Fix Validation Report

## Overview

Five buggy code snippets were corrected and validated.

- Python tests were executed using Python 3.
- C tests were compiled and executed using GCC.
- JavaScript tests were executed using GJS 1.78.0.
- All 15 documented tests passed.

## Bug 1 – Python Average Calculation

File: `bug1_fixed.py`

Test 1:
- Input: `[80, 90, 75, 85]`
- Expected output: `82.5`
- Actual output: `82.5`
- Result: PASS

Test 2:
- Input: `[]`
- Expected output: `0`
- Actual output: `0`
- Result: PASS

Execution: Python 3

Overall: PASS (2/2 tests)

## Bug 2 – JavaScript Total Calculation

File: `bug2_fixed.js`

Fix:
- Replaced multiplication assignment with addition assignment (`+=`).
- Preserved the correct loop boundary condition.

Tests executed using GJS 1.78.0.

Test 1:
- Input: `[10, 20, 30]`
- Expected output: `60`
- Actual output: `60`
- Result: PASS

Test 2:
- Input: `[5]`
- Expected output: `5`
- Actual output: `5`
- Result: PASS

Test 3:
- Input: `[]`
- Expected output: `0`
- Actual output: `0`
- Result: PASS

Overall: PASS (3/3 tests)

## Bug 3 – Python Student Index Handling

File: `bug3_fixed.py`

Fix:
- Added checks for negative and out-of-range indexes.
- Return `None` when the requested student does not exist.

Test 1:
- Input index: `2`
- Expected output: `Murad`
- Actual output: `Murad`
- Result: PASS

Test 2:
- Input index: `5`
- Expected output: `None`
- Actual output: `None`
- Result: PASS

Test 3:
- Input index: `-1`
- Expected output: `None`
- Actual output: `None`
- Result: PASS

Execution: Python 3

Overall: PASS (3/3 tests)

## Bug 4 – C Array Sum

File: `bug4_fixed.c`

Fix:
- Changed the loop condition from `i <= size` to `i < size`.

Compilation:
`gcc -Wall -Wextra -Werror`

Test 1:
- Input: `[10, 20, 30, 40, 50]`
- Expected output: `150`
- Actual output: `150`
- Result: PASS

Test 2:
- Input: `[7]`
- Expected output: `7`
- Actual output: `7`
- Result: PASS

Test 3:
- Input: zero elements
- Expected output: `0`
- Actual output: `0`
- Result: PASS

Execution: Successful

Overall: PASS (3/3 tests)

## Bug 5 – JavaScript Numeric Sorting

File: `bug5_fixed.js`

Fix:
- Added a numeric comparison function `(a, b) => a - b`.
- Used the spread operator to preserve the original array.

Tests executed using GJS 1.78.0.

Test 1:
- Input: `[100, 25, 3, 45, 9]`
- Expected output: `[3, 9, 25, 45, 100]`
- Actual output: `[3, 9, 25, 45, 100]`
- Result: PASS

Test 2:
- Input: `[1, 2, 3]`
- Expected output: `[1, 2, 3]`
- Actual output: `[1, 2, 3]`
- Result: PASS

Test 3:
- Input: `[]`
- Expected output: `[]`
- Actual output: `[]`
- Result: PASS

Test 4:
- Input: `[30, 10, 20]`
- Expected behavior: Original array remains unchanged after sorting.
- Actual behavior: Original array remains `[30, 10, 20]`.
- Result: PASS

Overall: PASS (4/4 tests)

## Final Summary

| Bug | Language | Tests Passed | Status |
|---|---|---:|---|
| Bug 1 | Python | 2/2 | PASS |
| Bug 2 | JavaScript (GJS) | 3/3 | PASS |
| Bug 3 | Python | 3/3 | PASS |
| Bug 4 | C | 3/3 | PASS |
| Bug 5 | JavaScript (GJS) | 4/4 | PASS |

Total tests: 15
Passed: 15
Failed: 0

Final result: PASS

Note: JavaScript validation was performed with GJS 1.78.0. The test harnesses executed the corrected functions independently; Node.js was not available.
