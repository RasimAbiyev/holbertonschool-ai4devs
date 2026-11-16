# SafeLens – System Architecture

## 1. Overview

SafeLens is a lightweight, local-first LLM safety evaluation platform.

The system uses a React frontend, a Python FastAPI backend, SQLite for persistent storage, and Ollama for local LLM inference.

## 2. High-Level Architecture

    flowchart TD
        U[User / AI Engineer]
        UI[React Frontend]
        API[FastAPI Backend]
        DB[(SQLite Database)]
        EVAL[Evaluation Engine]
        OLLAMA[Ollama Local API]
        MODEL[Local LLM]

        U --> UI
        UI <--> API
        API <--> DB
        API --> EVAL
        EVAL <--> OLLAMA
        OLLAMA --> MODEL

## 3. Main Components

### Frontend
- Provides the main SafeLens interface.
- Displays available test cases.
- Allows users to select a local model and start evaluations.
- Displays evaluation metrics and individual results.
- Supports manual review and report downloads.

### Backend – FastAPI
- Provides REST API endpoints.
- Manages test cases and evaluation runs.
- Coordinates model execution.
- Stores model responses and evaluation results.
- Calculates evaluation metrics.
- Generates JSON and CSV reports.

### Evaluation Engine
- Retrieves selected test cases.
- Sends prompts to the selected Ollama model.
- Collects model responses.
- Applies predefined evaluation rules.
- Records pass, fail, and error outcomes.
- Supports manual review.

### Database – SQLite
- Stores test cases.
- Stores evaluation runs.
- Stores individual evaluation results.
- Stores manual review status.

### Ollama Integration
- Connects to the local Ollama API.
- Retrieves available local models.
- Sends evaluation prompts to selected models.
- Returns generated responses to the backend.

## 4. Main Data Flow

1. The user opens the SafeLens web interface.
2. The frontend requests available test cases and local models.
3. The user selects a model and starts an evaluation.
4. FastAPI creates an evaluation run.
5. The evaluation engine retrieves the selected test cases.
6. The engine sends prompts to Ollama.
7. Ollama returns model responses.
8. The backend evaluates and stores the results.
9. The dashboard displays evaluation metrics.
10. The user can review individual responses or export reports.

## 5. Technology Stack

| Component | Technology |
|---|---|
| Frontend | React |
| Styling | Tailwind CSS |
| Backend | Python, FastAPI |
| Database | SQLite |
| Local LLM Runtime | Ollama |
| API Communication | REST / JSON |
| Testing | pytest, Playwright |
| Version Control | Git / GitHub |

## 6. MVP Constraints

- The application runs locally during the initial MVP stage.
- Ollama must be installed and accessible on the host machine.
- No paid external AI APIs are required.
- The first version supports a single-user workflow.
- SQLite is used to avoid external database infrastructure.
- Advanced authentication, cloud deployment, and distributed evaluation are outside the initial MVP scope.
