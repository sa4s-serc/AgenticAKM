### ADR-001: Use MLflow for MLOps Lifecycle Management

**Status:** Inferred
**Context:** In any machine learning project, it's critical to track experiments to compare model performance, manage model versions, and ensure that results are reproducible. Without a dedicated system, this information (hyperparameters, metrics, code versions, and model files) becomes scattered and difficult to manage, hindering collaboration and deployment readiness. The challenge is to establish a systematic and standardized process for the MLOps lifecycle.
**Decision:** The project has adopted **MLflow** as the central platform for experiment tracking and model management. The presence of the `mlruns` directory, with its detailed structure containing logged `params`, `metrics`, `tags`, and versioned model `artifacts` (including `MLmodel` files), is direct evidence of this decision. MLflow is being used to capture the entire context of each training run.
**Consequences:**
*   **Positive:**
    *   **Reproducibility:** Every experiment's parameters, performance metrics, and environment (`conda.yaml`, `requirements.txt`) are automatically logged, making it possible to reproduce results.
    *   **Standardization:** The MLflow Model format (`MLmodel`, `model.pkl`) provides a standardized way to package models, simplifying downstream deployment and serving.
    *   **Organization:** Provides a centralized and queryable repository for all experimental runs, which is crucial for comparing models and making informed decisions.
*   **Negative:**
    *   **Introduced Dependency:** The project now depends on the MLflow library and its associated concepts, requiring team members to be familiar with it.
    *   **Local Storage by Default:** The file-based backend shown (`mlruns` directory) is suitable for single-user development but does not scale well for teams. A remote tracking server would be needed for collaborative work, adding operational overhead.