# Bug Descriptions

This document describes the intended behavior and known symptoms of five
intentionally flawed code snippets prepared for the Smart Bug Bounty project.

## bug1.py

- **Language:** Python
- **Intended Behavior:** Return the last `n` items from a list.
- **Current Issue:** The slice excludes the final element. It also returns
  the entire list when `n` is zero instead of returning an empty list.
- **Bug Category:** Logic error / off-by-one error.

## bug2.js

- **Language:** JavaScript
- **Intended Behavior:** Calculate the total price, including tax, for all
  items and return the completed numeric result.
- **Current Issue:** The asynchronous callbacks inside `forEach` are not
  awaited. The function returns before the tax calculations finish.
- **Bug Category:** Asynchronous control-flow error.

## bug3.java

- **Language:** Java
- **Intended Behavior:** Calculate and return the arithmetic average of
  the values in an integer array as a double.
- **Current Issue:** Integer division occurs before the result is converted
  to a double, causing fractional parts to be lost.
- **Bug Category:** Numeric precision / type conversion error.

## bug4.c

- **Language:** C
- **Intended Behavior:** Calculate the sum of all elements in an array
  without accessing memory outside its bounds.
- **Current Issue:** The loop condition uses `i <= length`, which accesses
  one element beyond the valid array range.
- **Bug Category:** Memory safety / out-of-bounds access.

## bug5.py

- **Language:** Python
- **Intended Behavior:** Add an item to a collection. Each function call
  without an explicitly supplied collection should use a new empty list.
- **Current Issue:** The default list is created once and shared between
  calls, so items from earlier calls remain in later results.
- **Bug Category:** Mutable default argument.
