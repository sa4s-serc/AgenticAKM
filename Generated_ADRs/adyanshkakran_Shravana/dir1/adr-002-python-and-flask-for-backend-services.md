---
### ADR-002: Python and Flask for Backend Services

**Status:** Inferred
**Context:** The system required a backend to handle business logic, process data, and integrate with third-party services like WhatsApp and OpenAI. The backend needed to be developed quickly and leverage the rich ecosystem of libraries available for AI and data processing.
**Decision:** The backend service was implemented in Python using the Flask microframework. This is inferred from the `whatsapp-bot` directory structure, the `requirements.txt` file listing `flask`, and multiple `.py` files containing the server-side logic.
**Consequences:**
*   **Positive:**
    *   **Rapid Development:** Flask is a lightweight and unopinionated framework, which allows for fast prototyping and development.
    *   **Rich AI/ML Ecosystem:** Python is the de facto language for machine learning, providing seamless integration with libraries like `openai`, `speechrecognition`, and others.
    *   **Simplicity:** Flask's simplicity makes it easy to learn and maintain, especially for smaller services or APIs.
*   **Negative:**
    *   **Scalability for CPU-bound tasks:** Python's Global Interpreter Lock (GIL) can be a bottleneck for true parallelism in multi-threaded, CPU-intensive operations.
    *   **Lack of Structure:** Being unopinionated, Flask requires developers to enforce their own structure and conventions, which can lead to inconsistency in larger projects if not managed carefully.