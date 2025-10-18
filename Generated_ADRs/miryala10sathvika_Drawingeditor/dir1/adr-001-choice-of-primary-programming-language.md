### ADR-001: Choice of Primary Programming Language

**Status:** Inferred
**Context:** The project required a programming language to implement its core logic. The choice would influence development speed, performance, and the ecosystem of available tools and libraries. The presence of files like `draw.py` suggests a need for scripting capabilities, possibly for graphical or data processing tasks.
**Decision:** Python was chosen as the primary programming language for the application's logic. This is directly inferred from the existence of Python source code files (`draw.py`, `extra.py`).
**Consequences:**
*   **Positive:** Enables rapid development due to simple syntax and a rich standard library. Offers broad platform compatibility and a large community for support.
*   **Negative:** May face performance limitations for highly CPU-intensive tasks compared to compiled languages. The Global Interpreter Lock (GIL) in CPython can be a bottleneck for true parallel processing.
*   **Trade-off:** Developer productivity and ease of use were prioritized over maximum computational performance.