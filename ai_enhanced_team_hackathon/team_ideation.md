# Team Ideation

## 1. Brainstormed Ideas

### Idea 1: Multilingual AI Safety Evaluation Dashboard
A platform that evaluates AI models across multiple languages using safety, harmful-request handling, prompt injection resistance, and robustness tests.

### Idea 2: AI-Powered Document Intelligence
A tool that extracts key information, summarizes documents, and answers questions about uploaded files using retrieval-based techniques.

### Idea 3: AI Code Review Assistant
An application that analyzes source code, identifies potential bugs, explains security risks, and suggests improvements with AI assistance.

## 2. Chosen Idea

**Multilingual AI Safety Evaluation Dashboard**

## 3. Problem Statement

AI models can produce inconsistent or unsafe responses when handling harmful requests, adversarial prompts, and multilingual inputs. Their safety performance may vary across languages, particularly in languages with fewer available evaluation resources.

Developers need a practical way to test, compare, and understand AI model behavior across different safety scenarios.

Our solution is a lightweight evaluation dashboard that runs structured safety tests against AI models, records their responses, and presents measurable results. The MVP will prioritize multilingual evaluation, including Azerbaijani and English.

## 4. MVP Features

1. Test Case Management: Run predefined test cases covering benign requests, harmful requests, and prompt injection scenarios.
2. Multilingual Evaluation: Support Azerbaijani and English test inputs.
3. AI Model Integration: Evaluate responses from locally available models through Ollama.
4. Safety Scoring: Classify responses using predefined evaluation criteria and calculate pass/fail results.
5. Results Dashboard: Display evaluation summaries, safety scores, and language-based comparisons.

## 5. Proposed Technology Stack

- Programming Language: Python
- Backend: FastAPI
- Frontend: Streamlit
- AI Runtime: Ollama
- Data Storage: JSON / SQLite
- Testing: pytest
- Version Control: Git and GitHub

## 6. Team Roles

| Member | Role | Responsibilities |
|---|---|---|
| Team Member 1 | Team Lead & AI Engineer | Define scope, coordinate development, implement evaluation logic |
| Team Member 2 | Backend Developer | Build API endpoints and evaluation pipeline |
| Team Member 3 | Frontend Developer | Develop dashboard and results visualization |
| Team Member 4 | QA & Documentation Lead | Prepare test cases, validate outputs, document results and deployment |

*Team member names will be added after team assignments are confirmed.*

## 7. Expected Hackathon Outcome

A working web-based MVP that allows users to run multilingual AI safety evaluations, inspect model responses, and compare evaluation results through a simple dashboard.

The project will demonstrate how AI-assisted development, structured testing, and team collaboration can accelerate the development of a practical AI safety evaluation tool.

## 8. Success Criteria

- The application runs successfully.
- Users can execute predefined evaluation scenarios.
- Azerbaijani and English test cases are supported.
- Evaluation results are recorded and displayed.
- The team delivers a live demo within the hackathon timeframe.
