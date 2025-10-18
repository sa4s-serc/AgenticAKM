---
### ADR-002: Adoption of a Script-Based Processing Pipeline

**Status:** Inferred
**Context:** The system's functionality appears to follow a sequential workflow: data preparation (`shuffle_frames.py`), feature extraction (`extract_features.py`), model training (e.g., `svm_train.py`), and finally, inference or search (`find_closest2.py`). The architecture needed to support this step-by-step process in a simple and direct manner.
**Decision:** The system is structured as a collection of independent, single-purpose scripts. Each script represents a distinct stage in a data processing pipeline. It is likely that data is passed between these stages via the file system (e.g., CSV files, pickled objects, or image files).
**Consequences:**
*   **Positive:**
    *   The architecture is simple to understand and implement.
    *   Each stage of the pipeline can be developed, tested, and executed independently, which is excellent for debugging and experimentation.
    *   Allows for easy substitution of components (e.g., swapping `svm_train.py` for `linear_reg_train.py`).
*   **Negative:**
    *   The system can be inefficient due to I/O overhead as intermediate data is written to and read from disk between steps.
    *   There is no central orchestration, making the overall workflow implicit and potentially brittle. Managing dependencies and execution order relies on external tooling or manual intervention.