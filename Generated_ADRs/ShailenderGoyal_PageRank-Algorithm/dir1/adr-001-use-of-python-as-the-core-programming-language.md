### ADR-001: Use of Python as the Core Programming Language

**Status:** Inferred
**Context:** The project required a choice of programming language. The decision would influence development speed, available libraries, and the overall complexity of the application. The presence of a `.py` file indicates a need for a language that is well-suited for scripting, rapid prototyping, and general-purpose development.
**Decision:** Python was chosen as the programming language for this project. The core logic is implemented in the `project.py` file.
**Consequences:**
*   **Positive:** Enables rapid development due to simple syntax and dynamic typing. Python's extensive standard library allows for significant functionality without external dependencies. It has a large community and excellent documentation, making it easy to find support.
*   **Negative:** As an interpreted language, Python may have performance limitations for CPU-bound tasks compared to compiled languages. The Global Interpreter Lock (GIL) can also be a bottleneck for certain types of concurrent applications.