# Benchmark Tasks

## Purpose
Compare manual coding and GitHub Copilot-assisted coding using the same Python tasks and acceptance criteria.

## Task 1 — User Input Validation
**Estimated time:** 15–20 minutes

**Requirements:** Implement `validate_user(name, email, age)`. Validate non-empty names, basic email format, and integer age >= 18. Collect all errors.

**Inputs:** Name (string), email (string), age (integer).

**Output:** Dictionary containing `valid` (boolean) and `errors` (list).

**Acceptance Criteria:**
- Valid data returns `valid: True`.
- Invalid name, email, or age is rejected.
- Multiple errors are collected.

## Task 2 — Transaction Summary Analyzer

**Estimated time:** 20–25 minutes

**Requirements:** Implement `summarize_transactions(transactions)`. Calculate total amount, transaction count, and category totals. Reject negative amounts, missing fields, invalid amounts, and empty categories.

**Inputs:** A list of transaction dictionaries. Each dictionary contains `amount` (number) and `category` (string).

**Outputs:** A dictionary with `total_amount`, `transaction_count`, and `category_totals`.

**Acceptance Criteria:**
- Calculates correct total and category amounts.
- Counts transactions correctly.
- Rounds monetary values to two decimal places.
- Handles an empty list.
- Rejects invalid transactions.

## Task 3 — Task Priority Manager

**Estimated time:** 20–30 minutes

**Requirements:** Implement `manage_tasks(tasks, include_completed=False)`. Sort tasks by priority: high, medium, low. Preserve original order for equal priorities. Exclude completed tasks by default.

**Inputs:** A list of task dictionaries containing `id`, `title`, `priority`, and `completed`. The optional `include_completed` parameter is boolean.

**Outputs:** A list of task dictionaries sorted and filtered by the specified rules.

**Acceptance Criteria:**
- Sorts tasks in high, medium, low priority order.
- Preserves order among tasks with equal priority.
- Excludes completed tasks by default.
- Includes completed tasks when requested.
- Rejects missing or invalid fields and unsupported priorities.
- Returns an empty list for empty input.

## Benchmark Execution Guidelines

Complete each task twice: first without AI assistance, then with GitHub Copilot.

Record the following metrics for each attempt:
- Completion time in minutes.
- Lines of code written.
- Number of tests passed.
- Number of defects identified.
- Whether all acceptance criteria were satisfied.

Use identical requirements and acceptance criteria for both attempts.
