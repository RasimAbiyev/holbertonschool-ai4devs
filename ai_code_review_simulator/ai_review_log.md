# AI Code Review Log

## Project
Python Code Review Analyzer

## Objective
Develop a static Python code review tool using the built-in AST module.

## Implemented Checks
- Mutable default arguments
- Bare except clauses
- Use of eval() and exec()
- subprocess calls with shell=True
- Potentially unsafe pickle.load() and pickle.loads() usage

## Development and Testing
The analyzer was implemented using Python's ast.NodeVisitor.
Import aliases are tracked to identify relevant subprocess and pickle calls.
The analyzer resets its internal state between analysis runs.
Unit tests cover detected issues and cases where imports are absent.

## Test Results
- Total unit tests: 27
- Passed: 27
- Failed: 0

## Limitations
This is a static AST-based analyzer, not a complete security scanner.
It does not perform full data-flow analysis or resolve all dynamic imports,
variable assignments, and scope-related alias changes.
