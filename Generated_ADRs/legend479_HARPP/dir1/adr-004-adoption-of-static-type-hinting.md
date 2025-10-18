---
### ADR-004: Adoption of Static Type Hinting

**Status:** Inferred
**Context:** As a dynamically typed language, Python does not enforce variable or function signature types at compile time. In a project with a defined data model (`shapes.py`, `object.py`), this can lead to runtime errors and make the codebase harder to understand and refactor.
**Decision:** The project will use Python's standard type hints to improve code clarity and enable static analysis. This decision is inferred from the explicit inclusion of `typing` in the `requirements.txt` file. While `typing` is a standard library, its explicit listing suggests a conscious decision to prioritize its use and ensure compatibility.
**Consequences:**
*   **Positive:** Code becomes more self-documenting, making it easier for developers to understand function arguments and return values. It enables the use of static analysis tools (like mypy) to catch potential bugs before the code is run. IDEs can provide better autocompletion and error-checking.
*   **Negative:** Writing type hints adds a degree of verbosity to the code. It requires developers to be familiar with the `typing` module. The type hints are not enforced at runtime by default, so the benefits are only fully realized if static analysis tools are integrated into the development workflow.