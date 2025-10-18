---
### ADR-005: Component-Based Unit Testing

**Status:** Inferred
**Context:** To ensure the correctness and stability of the interpreter, especially as new language features are added or existing code is refactored, a robust and reliable testing strategy is essential.
**Decision:** A strategy of writing isolated unit tests for each major component of the interpreter pipeline was adopted. This is demonstrated by the presence of dedicated test files that mirror the core components: `lexer_test.py`, `parser_test.py`, and `eval_test.py`.
**Consequences:**
*   **Positive:** This approach makes it easier to pinpoint the source of bugs to a specific stage (e.g., a lexing error vs. a parsing error). It creates a safety net that allows for confident refactoring and provides clear, executable documentation for how each component is expected to behave.
*   **Negative:** This strategy focuses on individual units and does not eliminate the need for higher-level integration tests to ensure the components work together correctly. Writing and maintaining a comprehensive suite of unit tests requires a consistent time investment.