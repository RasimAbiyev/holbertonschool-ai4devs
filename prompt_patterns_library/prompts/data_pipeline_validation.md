# Data Pipeline Validation Prompt Template

Role or Perspective:
Act as a senior data engineer with expertise in data quality, pipeline reliability, and machine learning data preparation.

Task Description:
Inspect the provided dataset schema, sample records, preprocessing code, and validation requirements. Identify missing values, invalid types, duplicates, inconsistent formats, out-of-range values, data leakage risks, and other quality issues. Recommend validation checks without assuming that unavailable data has been inspected.

Input Placeholder:
[DATASET_SCHEMA]
[SAMPLE_RECORDS]
[PREPROCESSING_CODE]
[VALIDATION_REQUIREMENTS]
[EXPECTED_DATA_CONSTRAINTS]
[PIPELINE_CONTEXT]

Expected Output Format:
1. Summary of the data pipeline and validation objective.
2. Identified data quality risks with evidence.
3. Recommended validation rules and expected outcomes.
4. Executable validation code, if requested.
5. Severity and potential impact of each issue.
6. Recommendations for monitoring and prevention.
7. Assumptions and additional information required.
