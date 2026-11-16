# User Stories

## Project: Multilingual AI Safety Evaluation Dashboard

### US-01: Select an AI Model
As a user, I want to select an available local AI model so that I can evaluate its responses.

Acceptance Criteria:
- The application displays available configured models.
- The user can select a model before starting an evaluation.
- An unavailable model produces a clear error message.

### US-02: Run Safety Test Cases
As a user, I want to execute predefined safety test cases so that I can assess model behavior.

Acceptance Criteria:
- Test cases are grouped by category.
- The user can start an evaluation.
- The application records the model response for each test.

### US-03: Evaluate Multiple Languages
As a user, I want to run tests in Azerbaijani and English so that I can compare multilingual model behavior.

Acceptance Criteria:
- Test cases include Azerbaijani and English inputs.
- Each test records its language.
- Results can be filtered by language.

### US-04: Test Different Safety Categories
As a user, I want to evaluate benign requests, harmful requests, and prompt injection scenarios so that I can examine different safety behaviors.

Acceptance Criteria:
- Each test case has a category.
- The evaluation displays the category of each test.
- Results can be grouped by category.

### US-05: Inspect Model Responses
As a user, I want to inspect the original model responses so that I can understand why a test passed or failed.

Acceptance Criteria:
- Each completed test displays the model response.
- The response is linked to its test case.
- Failed or uncertain results can be inspected individually.

### US-06: View Evaluation Scores
As a user, I want to see evaluation results and safety scores so that I can understand the model's performance.

Acceptance Criteria:
- The dashboard displays passed, failed, and inconclusive test counts.
- Results include an overall score.
- The scoring criteria are documented and transparent.

### US-07: Compare Evaluation Runs
As a user, I want to compare evaluation runs from different models so that I can identify differences in their behavior.

Acceptance Criteria:
- Each evaluation run stores its model name.
- The user can view results from previous runs.
- The dashboard provides a basic comparison of scores.

### US-08: Review Evaluation History
As a user, I want to access previously completed evaluations so that I can review results without running the tests again.

Acceptance Criteria:
- Evaluation runs are stored locally.
- The user can open a previous run.
- Each run includes its date, model, and results.

### US-09: Handle Evaluation Errors
As a user, I want the application to report model connection and execution errors so that I can understand incomplete evaluations.

Acceptance Criteria:
- Connection errors are displayed clearly.
- Failed test executions are recorded.
- An error is not automatically classified as a safety pass.

## MVP Priority

- Must Have: US-01, US-02, US-03, US-04, US-05, US-06.
- Should Have: US-07, US-08.
- Additional: US-09.
