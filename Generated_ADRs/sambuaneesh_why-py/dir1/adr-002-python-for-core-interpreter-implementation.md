---
### ADR-002: Python for Core Interpreter Implementation

**Status:** Inferred
**Context:** A programming language needed to be selected for implementing the core logic of the interpreter (lexer, parser, evaluator). The choice would directly impact development speed, performance, and portability.
**Decision:** Python was chosen as the implementation language for the core interpreter. This is evident from the `.py` file extension used for all core logic files (`lexer.py`, `parser.py`, `eval.py`, `main.py`, etc.).
**Consequences:**
*   **Positive:** Python's high-level nature, dynamic typing, and powerful built-in data structures are well-suited for tasks like string manipulation (lexing) and tree construction (parsing), likely leading to faster development and more readable code.
*   **Negative:** As an interpreted language itself, Python will result in a slower execution speed for the new language compared to an implementation in a compiled language like C++ or Rust. This decision prioritizes developer productivity and simplicity over raw runtime performance.