# Code Fix Validation Report

## Overview

Five buggy code snippets were corrected and saved in this directory.
Python and C fixes were executed and tested.
JavaScript fixes were reviewed, but runtime testing was unavailable because Node.js is not installed.

## Bug 1 – Python Average Calculation

File: `bug1_fixed.py`

Tests:
1. Input: `[80, 90, 75, 85]`
   Expected: `82.5`
   Actual: `82.5`
   Result: PASS

2. Input: `[]`
   Expected: `0`
   Actual: `0`
   Result: PASS

Execution: Python 3
Overall: PASS (2/2 tests)

## Bug 2 – JavaScript Total Calculation

File: `bug2_fixed.js`

Fix:
- Replaced multiplication assignment with addition assignment (`+=`).
- Preserved the loop boundary condition.

Validation:
- Source code reviewed.
- Runtime execution not performed because Node.js is unavailable.

Expected test:
- Input: `[10, 20, 30]`
- Expected total: `60`
- Runtime status: NOT TESTED

## Bug 3 – Python Student Index Handling

File: `bug3_fixed.py`

Tests:
1. Index `2`
   Expected: `Murad`
   Actual: `Murad`
   Result: PASS

2. Index `5`
   Expected: `None`
   Actual: `None`
   Result: PASS

3. Index `-1`
   Expected: `None`
   Actual: `None`
   Result: PASS

Execution: Python 3
Overall: PASS (3/3 tests)

## Bug 4 – C Array Sum

File: `bug4_fixed.c`

Fix:
- Changed the loop condition from `i <= size` to `i < size`.

Tests:
1. Array `[10, 20, 30, 40, 50]`
   Expected: `150`
   Actual: `150`
   Result: PASS

2. Single-element array `[7]`
   Expected: `7`
   Actual: `7`
   Result: PASS

3. Zero elements
   Expected: `0`
   Actual: `0`
   Result: PASS

Compilation:
`gcc -Wall -Wextra -Werror`

Execution: Successful
Overall: PASS (3/3 tests)

## Bug 5 – JavaScript Numeric Sorting

File: `bug5_fixed.js`

Fix:
- Added a numeric comparison function `(a, b) => a - b`.
- Used the spread operator to preserve the original array.

Validation:
- Source code reviewed.
- Runtime execution not performed because Node.js is unavailable.

Expected input:
`[100, 25, 3, 45, 9]`

Expected sorted output:
`[3, 9, 25, 45, 100]`

Runtime status: NOT TESTED

## Final Summary

- Bug 1: PASS (2/2 tests)
- Bug 2: Source reviewed; runtime not tested
- Bug 3: PASS (3/3 tests)
- Bug 4: PASS (3/3 tests)
- Bug 5: Source reviewed; runtime not tested

Total executed tests: 8
Passed executed tests: 8

JavaScript runtime validation remains pending because Node.js is unavailable in the environment.
File: `bug3_fixed.py`

Tests:
1. Index `2` → Expected: `Murad` → Actual: `Murad` → PASS
2. Index `5` → Expected: `None` → Actual: `None` → PASS
3. Index `-1` → Expected: `None` → Actual: `None` → PASS

Execution: Python 3
Overall: PASS (3/3 tests)

