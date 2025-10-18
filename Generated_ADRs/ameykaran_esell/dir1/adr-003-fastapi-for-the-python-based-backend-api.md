---
### ADR-003: FastAPI for the Python-based Backend API

**Status:** Inferred
**Context:** The backend requires a high-performance web framework to serve API requests, handle potentially long-running I/O-bound tasks (like calling third-party AI APIs), and leverage Python's rich ecosystem for machine learning and data processing.
**Decision:** The backend API is built using FastAPI, a modern Python web framework. This is confirmed by the presence of `fastapi` and `uvicorn` in `requirements.txt`.
**Consequences:**
*   **Positive:**
    *   **High Performance:** FastAPI is built on Starlette and Pydantic and supports asynchronous code, making it highly efficient for I/O-bound operations and concurrent requests.
    *   **Developer Productivity:** It provides automatic data validation, serialization, and interactive API documentation (Swagger UI/ReDoc), which speeds up development and testing.
    *   **Ecosystem Access:** It allows the project to seamlessly integrate powerful Python libraries for AI (`google-genai`), PDF manipulation (`PyMuPdf`), and media creation (`manim`).
*   **Negative:**
    *   Leveraging the full potential of FastAPI requires an understanding of Python's `asyncio` library, which can introduce complexity for developers unfamiliar with asynchronous programming.