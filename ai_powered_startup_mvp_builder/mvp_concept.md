# MVP Concept – SafeLens

## Problem Statement

AI developers and organizations increasingly rely on Large Language Models (LLMs), but evaluating their safety and robustness remains difficult.

Existing evaluation approaches may not adequately cover multilingual scenarios, harmful requests, prompt injection, and attempts to bypass safety instructions, particularly in languages such as Azerbaijani.

SafeLens aims to provide a lightweight platform for evaluating LLM safety through structured test cases, measurable results, and human review.

## Target Users

- AI and Machine Learning Engineers
- LLM application developers
- AI safety researchers
- Universities and research institutions
- Small companies developing AI-powered applications

## Core Features

1. **Benchmark Test Execution:** Run predefined safety and robustness test cases against locally available LLMs through Ollama.

2. **Multilingual Evaluation:** Organize test cases by language, initially supporting Azerbaijani, English, and Turkish.

3. **Evaluation Dashboard:** Display safety results, pass/fail rates, and performance breakdowns by language and test category.

4. **Manual Review:** Allow users to inspect model responses and mark evaluation results for further review.

5. **Report Export:** Export evaluation results and summaries in JSON and CSV formats.

## Constraints

- The initial MVP will focus on local LLM evaluation using Ollama.
- No paid API services or external API keys will be required.
- The initial benchmark will use a limited collection of predefined test cases.
- The first version will support a single-user workflow without authentication.
- Evaluation results will be treated as experimental measurements, not as formal security certifications.
- The initial implementation will prioritize functionality, reproducibility, and clear reporting over advanced automation.
