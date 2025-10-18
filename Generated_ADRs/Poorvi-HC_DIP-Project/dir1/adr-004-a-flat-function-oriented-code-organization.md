---
### ADR-004: A Flat, Function-Oriented Code Organization

**Status:** Inferred
**Context:** The project requires a way to organize its source code. Given the script-based nature and likely focus on research or a proof-of-concept, a complex directory structure might be considered overkill. The challenge is to structure the code in a way that is simple and reflects the distinct functional components.
**Decision:** Adopt a flat directory structure where each file corresponds to a major functional component of the system. Responsibilities are separated by file (e.g., `extract_features.py` handles only feature extraction, `svm_train.py` handles only SVM training) rather than by classes or modules within a structured package hierarchy.
**Consequences:**
*   **Positive:**
    *   The structure is extremely simple and has a low barrier to entry for new developers.
    *   It is easy to find the code responsible for a specific high-level task.
*   **Negative:**
    *   This approach does not scale well. As the project grows, the root directory will become cluttered, and discovering relationships between scripts becomes difficult.
    *   It discourages code reuse, potentially leading to utility functions being copied and pasted across multiple script files instead of being placed in a shared library.