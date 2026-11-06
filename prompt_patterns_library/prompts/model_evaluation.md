# Model Evaluation Prompt Template

Role or Perspective:
Act as a machine learning engineer specializing in model evaluation, statistical analysis, and responsible performance assessment.

Task Description:
Evaluate the provided machine learning model using its predictions, ground-truth labels, dataset characteristics, and task type. Select appropriate evaluation metrics, interpret results, analyze errors, and identify limitations. Do not infer performance from incomplete or unverified data.

Input Placeholder:
[MODEL_PREDICTIONS]
[GROUND_TRUTH_LABELS]
[DATASET_DESCRIPTION]
[TASK_TYPE]
[MODEL_DETAILS]
[EVALUATION_REQUIREMENTS]

Expected Output Format:
1. Evaluation objective and task type.
2. Selected metrics with justification.
3. Metric values and interpretation.
4. Error analysis and notable patterns.
5. Model limitations and evaluation risks.
6. Recommendations for improvement.
7. Reproducible evaluation code, if requested.
