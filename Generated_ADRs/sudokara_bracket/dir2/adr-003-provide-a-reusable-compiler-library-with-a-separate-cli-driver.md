---
### ADR-003: Provide a reusable compiler library with a separate CLI driver

Status: Inferred
Context: Compiler components live under include/llracket and lib, while a driver exists at tools/driver/LLRacket.cpp with its own CMake configuration. Tests invoke compilation/execution through scripts, implying a command-line entry point.
Decision: Expose compiler functionality as a library and implement a separate command-line driver in tools/driver.
Consequences:
- Positive: Decouples UI from core logic; enables reuse (e.g., future IDE integration); simplifies testing of both library and end-to-end behavior.
- Negative: Requires a stable internal API; potential duplication of argument parsing or orchestration logic.