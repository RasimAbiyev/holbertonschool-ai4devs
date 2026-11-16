# Pull Request: Add Python Code Review Analyzer

## Summary

Introduces a lightweight static code review analyzer for Python source files.
The analyzer uses Python's Abstract Syntax Tree (AST) to identify common
code quality and security issues and produces structured review findings.

## Changes

- Added `ReviewIssue` as a structured representation of review findings.
- Implemented `ReviewAnalyzer` using Python's AST visitor interface.
- Added detection for mutable default arguments.
- Added detection for bare exception handlers.
- Added detection for potentially unsafe `eval()` and `exec()` calls.
- Included source line numbers and severity levels in each finding.
- Added a text-based report formatter.
- Added 9 automated unit tests covering detection rules, clean code,
  line numbers, and report formatting.

## Context

This feature establishes the first review engine for the AI Code Review
Simulator project. It provides a deterministic baseline that can later
be compared with AI-generated and human code review feedback.

The implementation uses Python's standard library and requires no external
API keys or paid services.

## Testing

- Command: `python3 -m unittest -v`
- Result: 9 tests passed.
- Command: `python3 -m py_compile review_analyzer.py test_review_analyzer.py`
- Result: Passed without syntax errors.

## Scope

The implementation and tests contain approximately 159 lines of code.
This initial version focuses on a small set of Python review rules.
