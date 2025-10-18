---
### ADR-002: Adopt a Modular, Pipeline-based Architecture

**Status:** Inferred
**Context:** A typical machine learning task involves several distinct stages: data loading/processing, model definition, training, evaluation, and model saving. Implementing this entire workflow in a single, monolithic script leads to code that is difficult to read, test, maintain, and reuse. The architectural challenge is to structure the codebase in a way that reflects these distinct logical stages.
**Decision:** The project is structured into discrete, single-responsibility Python modules, indicating a **modular, pipeline-based architecture**. The file structure `linear_regression/data.py`, `model.py`, `train.py`, `eval.py`, and `save.py` clearly separates the different concerns of the ML workflow. The `pipeline.py` file likely acts as an orchestrator, executing these stages in a defined sequence.
**Consequences:**
*   **Positive:**
    *   **Improved Maintainability:** Changes to one stage (e.g., data loading logic in `data.py`) are isolated and less likely to break other parts of the system.
    *   **Enhanced Reusability:** Individual components, like the data loader, can be easily reused in other projects or pipelines.
    *   **Testability:** Each module can be unit-tested independently, leading to more robust and reliable code.
    *   **Clarity:** The structure makes the overall workflow easy to understand by mapping files to logical steps.
*   **Negative:**
    *   **Increased Complexity:** This approach introduces a slightly higher level of complexity in managing the data flow and dependencies between modules compared to a single script.