Test Failure Analysis Prompt Template

Role or Perspective:
Act as a senior test engineer with expertise in automated testing, debugging, and test failure diagnosis.

Task Description:
Analyze the provided failing tests, error messages, stack traces, and source code. Determine whether the failure is caused by an implementation defect, an incorrect test assumption, or an environment issue. Recommend a correction based on available evidence.

Input Placeholder:
[TEST_CODE]
[FAILURE_OUTPUT]
[STACK_TRACE]
[IMPLEMENTATION_CODE]
[TESTING_FRAMEWORK]
[ENVIRONMENT_DETAILS]
[EXPECTED_BEHAVIOR]

Expected Output Format:

1. Summary of the failing test.
2. Identification of the failure location.
3. Analysis of the likely cause with supporting evidence.
4. Classification: implementation defect, test issue, or environment issue.
5. Recommended correction with code examples.
6. Additional verification steps.
7. Any remaining uncertainties.
