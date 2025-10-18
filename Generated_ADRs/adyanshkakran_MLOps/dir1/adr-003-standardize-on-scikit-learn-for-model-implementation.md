---
### ADR-003: Standardize on Scikit-learn for Model Implementation

**Status:** Inferred
**Context:** The project requires a machine learning library to implement its regression models. The choice of library impacts development speed, performance, and integration with other tools. A decision was needed on a primary ML framework to ensure consistency across the project.
**Decision:** **Scikit-learn** was chosen as the machine learning framework. This is evidenced by `scikit-learn==1.2.2` in the `requirements.txt` file and the specific MLflow-logged hyperparameters (e.g., `n_estimators`, `max_depth`, `max_features`) which are characteristic of Scikit-learn's ensemble models like `RandomForestRegressor`.
**Consequences:**
*   **Positive:**
    *   **Rich Ecosystem:** Scikit-learn provides a comprehensive set of tools for data preprocessing, modeling, and evaluation with a consistent API (`fit`/`predict`).
    *   **Strong Integration:** It integrates seamlessly with the scientific Python stack (NumPy, Pandas) and MLOps tools like MLflow, whose autologging feature works exceptionally well with Scikit-learn estimators.
    *   **Ease of Use:** The library is well-documented and has a gentle learning curve, making it highly productive for a wide range of classical ML tasks.
*   **Negative:**
    *   **Scope Limitation:** While excellent for classical machine learning, Scikit-learn is not the primary choice for deep learning, which would require integrating other libraries like TensorFlow or PyTorch if needs change.