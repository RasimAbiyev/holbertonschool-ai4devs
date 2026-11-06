Prompt Use Cases

This document identifies recurring software development tasks where reusable AI prompt patterns can improve productivity, code quality, and reliability.

1. Code Quality

Refactoring

- Goal: Improve code readability, maintainability, and performance without changing existing behavior.
- Input: Source code in [LANGUAGE].
- Output: Refactored code, explanation of changes, and potential trade-offs.

Code Review

- Goal: Identify bugs, code smells, security issues, and maintainability problems.
- Input: Source code, relevant requirements, and coding standards.
- Output: Review findings categorized by severity, with suggested fixes.

Style Enforcement

- Goal: Apply consistent naming conventions, formatting, and coding standards.
- Input: Source code and [STYLE_GUIDE].
- Output: Revised code following the specified style guide.

2. Debugging

Error Analysis

- Goal: Identify the cause of an error and provide a reliable solution.
- Input: Error message, stack trace, source code, and environment details.
- Output: Root cause explanation and step-by-step fix.

Root Cause Analysis

- Goal: Investigate the underlying reason for unexpected application behavior.
- Input: Bug description, reproduction steps, logs, and relevant code.
- Output: Root cause, supporting evidence, and recommended solution.

Performance Debugging

- Goal: Identify performance bottlenecks and propose optimizations.
- Input: Code, performance measurements, and system constraints.
- Output: Bottleneck analysis, optimization suggestions, and expected impact.

3. Documentation

README Generation

- Goal: Create clear and useful project documentation.
- Input: Project structure, dependencies, features, and setup instructions.
- Output: A structured README.md with installation, usage, and contribution sections.

API Documentation

- Goal: Document API endpoints, parameters, responses, and error handling.
- Input: API source code, routes, schemas, and authentication requirements.
- Output: Structured API documentation with request and response examples.

4. Testing

Unit Test Generation

- Goal: Generate unit tests covering expected behavior and important edge cases.
- Input: Source code, function specifications, and testing framework [FRAMEWORK].
- Output: Executable unit tests with clear test names and assertions.

Edge Case Identification

- Goal: Discover boundary conditions and unusual inputs that could cause failures.
- Input: Function implementation, expected behavior, and input constraints.
- Output: A list of edge cases with expected results and suggested tests.

Test Failure Analysis

- Goal: Diagnose failing tests and distinguish implementation defects from incorrect test assumptions.
- Input: Test code, failure output, stack trace, and implementation.
- Output: Failure explanation and recommended correction.

5. AI/ML Development

Model Evaluation

- Goal: Evaluate machine learning model performance using appropriate metrics.
- Input: Model predictions, ground-truth labels, dataset description, and task type.
- Output: Evaluation metrics, error analysis, limitations, and improvement recommendations.

Data Pipeline Validation

- Goal: Identify data quality problems before model training or inference.
- Input: Dataset schema, sample records, preprocessing code, and validation requirements.
- Output: Data quality checks, detected issues, and validation code.

Summary

This library covers 12 recurring use cases across five software development categories. These use cases provide a foundation for designing reusable prompt templates that can be tested, improved, and applied to real development workflows.
