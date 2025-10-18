### ADR-001: Multi-Stage Interpreter Pipeline

**Status:** Inferred
**Context:** The primary goal of the project is to create a programming language interpreter. A fundamental architectural challenge is how to process raw source code text and execute its logic. The system must transform text into a structured, understandable format before it can be evaluated.
**Decision:** The architecture employs a classic, multi-stage interpreter pipeline. The process is broken down into distinct, sequential phases:
1.  **Lexical Analysis:** Source code is converted into a stream of tokens (evidenced by `lexer.py` and `tok.py`).
2.  **Parsing:** The token stream is parsed into an Abstract Syntax Tree (AST), a hierarchical representation of the code's structure (evidenced by `parser.py` and `ast1.py`).
3.  **Evaluation:** The AST is traversed and executed, managing state within an environment (evidenced by `eval.py`, `object.py`, and `environment.py`).
**Consequences:**
*   **Positive:** This separation of concerns creates a highly modular and maintainable system. Each stage has a single responsibility, making it easier to develop, debug, and test in isolation (as seen with `lexer_test.py`, `parser_test.py`, etc.). It's a standard, well-understood pattern for language implementation, making it easier for new developers to comprehend.
*   **Negative:** This approach can introduce performance overhead compared to a single-pass interpreter, as it requires creating intermediate data structures (tokens, AST nodes) between each stage.