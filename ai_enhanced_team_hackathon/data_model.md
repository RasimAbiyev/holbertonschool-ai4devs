# Data Model

## Project: Multilingual AI Safety Evaluation Dashboard

The MVP uses SQLite for persistent storage. The data model contains three primary entities: TestCase, EvaluationRun, and TestResult.

## 1. Entity: TestCase

Stores predefined evaluation scenarios.

| Field | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| title | TEXT | Short test case title |
| prompt | TEXT | Input prompt sent to the model |
| language | TEXT | Test language, such as Azerbaijani or English |
| category | TEXT | Benign, harmful, or prompt injection |
| expected_behavior | TEXT | Expected safe model behavior |
| created_at | DATETIME | Record creation timestamp |

## 2. Entity: EvaluationRun

Stores an evaluation session for a selected AI model.

| Field | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| model_name | TEXT | Name of the evaluated model |
| started_at | DATETIME | Evaluation start time |
| completed_at | DATETIME | Evaluation completion time |
| total_tests | INTEGER | Number of executed tests |
| passed_tests | INTEGER | Number of tests passed |
| failed_tests | INTEGER | Number of tests failed |
| inconclusive_tests | INTEGER | Number of inconclusive tests |
| overall_score | REAL | Percentage score based on completed, classifiable tests |

## 3. Entity: TestResult

Stores the outcome of an individual test within an evaluation run.

| Field | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| run_id | INTEGER | Foreign key referencing EvaluationRun |
| test_case_id | INTEGER | Foreign key referencing TestCase |
| model_response | TEXT | Original response returned by the model |
| status | TEXT | Passed, failed, or inconclusive |
| evaluation_notes | TEXT | Explanation of the evaluation result |
| execution_time_ms | INTEGER | Model execution time in milliseconds |
| created_at | DATETIME | Result creation timestamp |

## Relationships

- One EvaluationRun can contain many TestResults.
- One TestCase can be referenced by many TestResults.
- Each TestResult belongs to one EvaluationRun and one TestCase.

## Relationship Summary

EvaluationRun (1) ---- (N) TestResult
TestCase (1) --------- (N) TestResult

## Data Integrity Rules

- Every TestResult must reference an existing EvaluationRun.
- Every TestResult must reference an existing TestCase.
- Test status must be Passed, Failed, or Inconclusive.
- An execution error must not be counted as a successful safety result.
- The overall score must use a documented denominator and exclude inconclusive results from the pass-rate calculation.

## MVP Storage Strategy

SQLite will store test cases, evaluation runs, and test results. JSON may be used for importing predefined test cases and exporting evaluation reports.
