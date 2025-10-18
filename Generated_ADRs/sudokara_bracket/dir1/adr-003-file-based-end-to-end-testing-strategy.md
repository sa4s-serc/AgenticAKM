---
### ADR-003: File-Based End-to-End Testing Strategy

**Status:** Inferred

**Context:** A compiler is a complex piece of software where correctness is paramount. It must correctly translate valid programs and provide clear errors for invalid ones. A robust testing strategy is needed to verify the behavior of the compiler across a wide range of language features and edge cases.

**Decision:** The project employs an extensive, file-based, end-to-end testing strategy. The `tests/` directory is organized by language feature (`functions`, `if`, `loops`, `vector`, etc.). For each test case (`.rkt` file), there are corresponding expected output (`.out`), expected error (`.err`), and optional input (`.in`) files. Scripts like `run_tests.sh` and `test_script.py` are used to automate the process of running the compiler on test files and comparing the actual output/error with the expected results.

**Consequences:**
*   **Positive:**
    *   **High Confidence:** Provides strong guarantees that the compiler as a whole behaves as expected for a large suite of inputs.
    *   **Regression Prevention:** Makes it easy to detect when a new change breaks existing functionality.
    *   **Clear Test Cases:** Test cases are self-contained and easy to understand, as the source, input, and expected output are all explicitly defined in files.
*   **Negative:**
    *   **Brittle Tests:** Tests can be sensitive to minor, benign changes in output formatting (e.g., extra whitespace).
    *   **Limited Unit-Level Insight:** This strategy primarily tests the entire compiler pipeline and may not easily pinpoint failures within a specific internal component without further debugging.