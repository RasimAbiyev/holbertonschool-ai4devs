# SafeLens – User Stories

## User Story 1: View Available Test Cases

As an AI engineer, I want to view predefined safety test cases so that I can understand which scenarios are available for evaluation.

**Acceptance Criteria:**
- The system displays available test cases.
- Each test case includes a description, language, and category.
- Test cases can be filtered by language and category.

## User Story 2: Select an LLM

As an AI engineer, I want to select a locally available Ollama model so that I can evaluate its safety without using paid external APIs.

**Acceptance Criteria:**
- The system lists available local Ollama models.
- The user can select a model before starting an evaluation.
- The system reports an error if the selected model is unavailable.

## User Story 3: Run a Safety Evaluation

As an AI engineer, I want to execute predefined safety tests against a selected model so that I can measure its responses to potentially harmful requests.

**Acceptance Criteria:**
- The user can start an evaluation.
- The system sends test prompts to the selected local model.
- Each response is stored with its corresponding test case.
- Execution errors are recorded.

## User Story 4: Evaluate Multiple Languages

As an AI safety researcher, I want to run tests in Azerbaijani, English, and Turkish so that I can compare model behavior across languages.

**Acceptance Criteria:**
- Test cases include a language field.
- Results can be filtered by language.
- The dashboard displays language-specific evaluation metrics.

## User Story 5: Evaluate Safety Categories

As an AI safety researcher, I want to organize tests by safety category so that I can identify weaknesses in specific areas.

**Acceptance Criteria:**
- Test cases support categories such as harmful requests, prompt injection, and robustness.
- Results can be filtered by category.
- Category-level metrics are available.

## User Story 6: View Evaluation Results

As an AI engineer, I want to view evaluation results in a dashboard so that I can understand the model's performance.

**Acceptance Criteria:**
- The dashboard displays total tests, passed tests, failed tests, and errors.
- Results can be grouped by language and category.
- The dashboard distinguishes failed tests from execution errors.

## User Story 7: Review Model Responses

As an AI safety researcher, I want to inspect individual model responses and mark them for manual review so that I can identify cases requiring human judgment.

**Acceptance Criteria:**
- The user can open an individual evaluation result.
- The original prompt and model response are visible.
- The user can mark a result as requiring review.
- The review status is saved.

## User Story 8: Export Evaluation Reports

As an AI engineer, I want to export evaluation results in JSON and CSV formats so that I can analyze or share the results outside SafeLens.

**Acceptance Criteria:**
- The user can export a completed evaluation.
- JSON and CSV formats are supported.
- Exported reports include model information, test cases, responses, and evaluation outcomes.

## User Story 9: Compare Evaluation Runs

As an AI researcher, I want to compare evaluation runs so that I can observe differences between models or test configurations.

**Acceptance Criteria:**
- The system stores previous evaluation runs.
- Each run records the selected model and execution date.
- The user can compare summary metrics from different runs.

## User Story 10: Handle Evaluation Errors

As an AI engineer, I want the system to report model connection failures and test execution errors so that I can identify and troubleshoot problems.

**Acceptance Criteria:**
- Connection failures are displayed clearly.
- Failed test executions are recorded.
- Errors do not silently disappear from evaluation reports.
