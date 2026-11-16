# High-Level Architecture Plan

## Project
Multilingual AI Safety Evaluation Dashboard

## 1. Architecture Overview
The application uses a layered architecture. Streamlit provides the frontend, FastAPI handles API requests, a Python evaluation service runs test cases, Ollama provides local AI models, and SQLite stores evaluation data.

## 2. Main Components

### Frontend - Streamlit
- Display the evaluation dashboard.
- Allow model and test category selection.
- Show responses, scores, and historical results.

### Backend - FastAPI
- Validate incoming requests.
- Provide API endpoints.
- Coordinate evaluation runs.
- Handle errors and return results.

### Evaluation Service - Python
- Load predefined test cases.
- Send prompts to the selected model.
- Collect responses and apply documented criteria.
- Classify results as Passed, Failed, or Inconclusive.
- Calculate evaluation metrics.

### AI Runtime - Ollama
- Provide access to locally available language models.
- Generate responses to evaluation prompts.
- Return responses to the evaluation service.

### Database - SQLite
- Store test cases, evaluation runs, model responses, and results.
- Support retrieval of historical evaluations.

## 3. Request Flow
1. User selects a model and test categories in Streamlit.
2. Streamlit sends a request to FastAPI.
3. FastAPI calls the Python evaluation service.
4. The service loads test cases and sends prompts to Ollama.
5. Ollama returns model responses.
6. The service evaluates responses using documented criteria.
7. Results are stored in SQLite.
8. FastAPI returns the summary to Streamlit.
9. Streamlit displays scores and results.

## 4. Architecture Diagram

Streamlit Frontend
       |
       v
FastAPI Backend
       |
       v
Python Evaluation Service
       |              |
       v              v
     Ollama         SQLite
  Local Models   Evaluation Data



## 5. Proposed API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | Check backend availability |
| GET | /models | List available local models |
| GET | /test-cases | Retrieve test cases |
| POST | /evaluations | Start an evaluation |
| GET | /evaluations | List previous runs |
| GET | /evaluations/{id} | Retrieve a specific run |

## 6. Testing Strategy
- Unit tests for evaluation logic and score calculation using pytest.
- API tests for FastAPI endpoints.
- Integration tests for Ollama when a local model is available.
- Manual frontend testing.
- Test Azerbaijani and English scenarios.

## 7. Security and Reliability
- Use local model execution to avoid paid external APIs.
- Treat model responses as untrusted data.
- Never execute generated code or commands from model responses.
- Record execution errors separately from safety failures.
- Keep evaluation criteria transparent and reproducible.
- Do not present automated scores as definitive proof of model safety.

## 8. 24-Hour Implementation Plan
- Phase 1: Create project structure, test case format, and SQLite database.
- Phase 2: Connect Ollama and implement the evaluation service.
- Phase 3: Build Streamlit dashboard and connect FastAPI.
- Phase 4: Test, fix critical issues, and prepare the demonstration.

## 9. Deployment Plan
The MVP will run locally during development and testing. A hosted demonstration may be prepared if the environment supports the backend and model runtime. Otherwise, the team will demonstrate the application locally and document the deployment limitation.

## 10. Known Limitations
- Initial language support is limited to Azerbaijani and English.
- The initial test case collection will be limited.
- Automated evaluation may produce false positives or false negatives.
- Results depend on the selected model and local runtime.
- Model comparisons must use the same test cases and scoring criteria.
