# ADR-002: Selection of Python for the Backend Processing Engine

**Date**: 2025-10-14
**Status**: Proposed

## Context
The backend's core responsibility is orchestrating AI-driven workflows, including interacting with LLM APIs, parsing documents, and running content generation scripts (e.g., for video). This requires a language with a mature ecosystem for AI/ML, data manipulation, and scripting.

## Decision
Python was chosen as the backend language. Its extensive libraries for AI (Google Gemini client), data validation (Pydantic), and web services (Flask/FastAPI) make it an ideal choice for orchestrating the content transformation pipelines.

## Consequences
This choice accelerates development by leveraging a vast ecosystem of pre-existing tools, making it easy to integrate with the LLM and other data services. The trade-off is that Python may face performance limitations for highly concurrent, CPU-bound tasks due to the Global Interpreter Lock (GIL), potentially requiring more complex scaling strategies for such workloads.