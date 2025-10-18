---
### ADR-004: Ensure Environment Reproducibility through Pinned Dependencies

**Status:** Inferred
**Context:** The behavior of machine learning models can be highly sensitive to the specific versions of the libraries used during training (e.g., NumPy, Scikit-learn). To ensure that a training run can be precisely replicated in the future, or that a deployed model behaves identically to its tested version, the execution environment must be strictly controlled.
**Decision:** The project enforces reproducibility by **pinning the exact versions of its Python dependencies**. This is clearly shown in the `requirements.txt` file, which uses the `==` specifier (e.g., `mlflow==2.3`, `scikit-learn==1.2.2`). This practice is further reinforced by MLflow's automatic logging of environment files (`conda.yaml`, `python_env.yaml`, `requirements.txt`) within each model artifact directory.
**Consequences:**
*   **Positive:**
    *   **High Fidelity Reproduction:** Guarantees that anyone running the project with the specified requirements will have the exact same environment, minimizing "works on my machine" issues.
    *   **Stable Deployments:** Prevents unexpected behavior in production caused by automatic updates to dependency packages.
*   **Negative:**
    *   **Maintenance Overhead:** Pinned dependencies must be actively managed and updated to incorporate security patches or new features from the upstream libraries.
    *   **Dependency Staleness:** If not regularly updated, the project could be left using outdated and potentially vulnerable versions of libraries.