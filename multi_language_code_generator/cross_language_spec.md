# Cross-Language Specification — Transaction Analyzer

## 1. Algorithm Description

Analyze financial transactions and calculate:
- Number of valid transactions.
- Number of rejected transactions.
- Total amount in cents.
- Total amount grouped by category.

Implementations must produce equivalent results in Python, JavaScript, and Go.

## 2. Input Format

A JSON array of transaction objects:
- `id`: non-empty string.
- `category`: non-empty string.
- `amount_cents`: non-negative integer.

## 3. Input Example

Example input:
[
  {"id": "T001", "category": "food", "amount_cents": 1500},
  {"id": "T002", "category": "transport", "amount_cents": 2500}
]

## 4. Output Format

A JSON object containing:
- `valid_transactions`: number of accepted transactions.
- `rejected_transactions`: number of rejected transactions.
- `total_amount_cents`: sum of accepted amounts.
- `category_totals`: category names mapped to their total amounts in cents.

Category names must be sorted alphabetically.

## 5. Validation Rules

- Transaction IDs must be non-empty strings.
- Category names must be non-empty strings.
- Amounts must be non-negative integers.
- Duplicate IDs are rejected; the first valid occurrence is retained.
- Invalid transactions must not affect totals.
- Empty input must produce zero counts and totals.

## 6. Edge Cases

- Empty transaction list.
- Negative transaction amount.
- Missing transaction fields.
- Empty ID or category.
- Duplicate transaction IDs.
- Zero transaction amount.
- Multiple transactions in the same category.

## 7. Test Cases

### Test 1 — Valid Transactions
Input: Two valid transactions:
- T001, food, 1500 cents
- T002, transport, 2500 cents

Expected output:
- valid_transactions: 2
- rejected_transactions: 0
- total_amount_cents: 4000
- category_totals: food=1500, transport=2500

### Test 2 — Empty Input
Input: Empty transaction list.

Expected output:
- valid_transactions: 0
- rejected_transactions: 0
- total_amount_cents: 0
- category_totals: empty object

### Test 3 — Negative Amount
Input: One transaction with amount_cents = -500.

Expected output:
- valid_transactions: 0
- rejected_transactions: 1
- total_amount_cents: 0
- category_totals: empty object

### Test 4 — Duplicate Transaction ID
Input:
- T001, food, 1500 cents
- T001, transport, 2500 cents

Expected output:
- valid_transactions: 1
- rejected_transactions: 1
- total_amount_cents: 1500
- category_totals: food=1500

### Test 5 — Empty Category
Input: One transaction with an empty category:
- T003, empty category, 1000 cents

Expected output:
- valid_transactions: 0
- rejected_transactions: 1
- total_amount_cents: 0
- category_totals: empty object

## 8. Cross-Language Consistency

All three implementations must:
- Accept the same JSON input format.
- Apply identical validation rules.
- Produce equivalent JSON output.
- Use integer cents to avoid floating-point rounding differences.
- Pass all five test cases.

