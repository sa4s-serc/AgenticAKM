---
### ADR-002: Separation of Offline Learning from Online Decision-Making

**Status:** Inferred
**Context:** The adaptation logic requires a "knowledge base" to make informed decisions (e.g., which model to use under which conditions). Generating this knowledge can be computationally expensive, involving training machine learning models and analyzing large datasets. Performing this complex learning process during runtime could severely impact the system's performance and responsiveness.
**Decision:** The architecture is split into two distinct phases: an offline "Learning Engine" and an online "Adaptation Engine."
*   **Offline Learning:** The `Learning Engine and Adaptation Rules/` directory contains Jupyter notebooks (`1_Optimal_K_Values.ipynb`, `2_Clustering_Rules.ipynb`), pickled models (`*_skmeans_model.pkl`), and raw data (`detection_results_*.txt`). This sub-system is responsible for processing data and training clustering models to generate adaptation rules.
*   **Online Decision-Making:** The runtime components (`AdaMLS` and `NAVIE`) consume the pre-computed outputs of the learning phase (e.g., the CSV files in `AdaMLS/Knowledge_get_cluster/`). The online decision-making process is thereby simplified to a fast lookup or simple inference using the pre-generated rules.
**Consequences:**
*   **Positive:**
    *   **Runtime Performance:** The online adaptation loop is lightweight and fast, as the computationally intensive learning is already completed. Decisions can be made with minimal latency.
    *   **Predictability:** The runtime behavior is more predictable since the adaptation rules are fixed and loaded at the start.
    *   **Robustness:** The system is not dependent on the success of a complex training process during live operation.
*   **Negative:**
    *   **Stale Knowledge:** The system cannot adapt to new conditions that were not present in the offline training data. The knowledge base becomes static and requires a full offline retraining cycle to be updated.
    *   **Operational Complexity:** Requires a two-stage deployment process: first run the learning engine to generate artifacts, then deploy the runtime engine with those artifacts.