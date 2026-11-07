# Reflection on AI-Assisted Debugging

## Introduction

In this project, I investigated five code snippets containing different types of bugs in Python, JavaScript, and C. I used an AI assistant to identify the problems, explain their root causes, and suggest possible solutions. After reviewing the suggestions, I implemented fixes and tested them using the available programming environments. The main purpose was to evaluate whether AI could make debugging more efficient while understanding where human judgment remained necessary.

## AI Strengths

The AI assistant performed well when identifying straightforward programming errors. For example, in `bug1.py`, it identified a missing colon after an `if` statement, which caused a syntax error. In `bug2.js`, it recognized that the multiplication assignment operator (`*=`) should have been addition assignment (`+=`) when calculating a total.

AI was also useful for explaining more complex issues. It identified the out-of-range array access in `bug3.py`, the incorrect loop condition in `bug4.c`, and the default lexicographical sorting behavior in `bug5.js`. These explanations helped connect the visible symptoms with their underlying causes.

Overall, AI reduced the time needed to investigate unfamiliar code and provided a useful starting point for each fix.

## AI Weaknesses

Although most suggestions were technically correct, not every initial solution was sufficient for reliable software. In `bug3.py`, the suggested correction used a valid list index, but this alone did not protect the function against other invalid indexes. A more robust solution required explicit boundary checks.

Similarly, fixing the sorting behavior in `bug5.js` required more than adding a numeric comparator. I also wanted to preserve the original array, so I used the spread operator before sorting. This demonstrated that an AI-generated fix may solve the immediate bug without necessarily addressing broader code-quality concerns.

AI suggestions therefore required verification rather than automatic acceptance.

## Human Role

Human judgment was essential when evaluating edge cases and deciding whether a fix was sufficiently robust. I reviewed the proposed changes, considered empty inputs, invalid indexes, single-element arrays, and preservation of original data.

I also selected appropriate validation methods for each language. Python tests, GJS-based JavaScript tests, and GCC compilation with warning checks were used. The final validation covered 15 test cases, all of which passed.

This process showed that understanding the requirements and choosing meaningful test cases cannot be delegated entirely to AI.

## Conclusion

AI-assisted debugging made the workflow faster by identifying likely causes and suggesting practical corrections. However, it was most effective as a collaborative tool rather than an independent developer. Its explanations were useful, but correctness, edge cases, and maintainability still required human review.

My trust level in AI suggestions is therefore moderate: I consider them valuable hypotheses that must be tested. In real-world development, AI can improve productivity, but developers remain responsible for validating fixes, understanding system behavior, and making final engineering decisions.
