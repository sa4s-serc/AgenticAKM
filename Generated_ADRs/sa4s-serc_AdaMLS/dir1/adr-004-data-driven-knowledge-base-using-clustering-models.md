---
### ADR-004: Data-Driven Knowledge Base Using Clustering Models

**Status:** Inferred
**Context:** The system needs to map observable environmental or input conditions to an optimal configuration (e.g., which YOLOv5 model to use). A simple, hardcoded set of `if-then-else` rules would be brittle and difficult to create and maintain, especially if the input space is complex.
**Decision:** The knowledge base for the adaptation logic is generated using a data-driven approach based on machine learning, specifically clustering. Files like `large_skmeans_model.pkl`, `2_Clustering_Rules.ipynb`, and `*_get_cluster.csv` indicate that:
1.  Detection results from different models are collected.
2.  A clustering algorithm (Spherical K-Means, based on `skmeans`) is trained to group similar input conditions.
3.  The resulting clusters and their mappings to optimal models are stored in easily parsable formats like CSV files (`*_get_cluster_mapping.csv`).
At runtime, the `Analyzer` or `Planner` can quickly determine the cluster for the current input and look up the best configuration from the pre-computed CSV files.
**Consequences:**
*   **Positive:**
    *   **Automated Rule Generation:** Eliminates the need for a human expert to manually define complex adaptation rules. The rules are learned directly from performance data.
    *   **Scalability:** The approach can handle a high-dimensional input space more effectively than manual rule-crafting.
    *   **Discoverability:** The clustering process may uncover non-obvious relationships between input characteristics and optimal model configurations.
*   **Negative:**
    *   **Interpretability:** The "rules" embodied by the cluster mappings may be difficult for a human to interpret, making debugging the adaptation logic more challenging.
    *   **Dependence on Data Quality:** The effectiveness of the entire adaptation system is highly dependent on the quality and representativeness of the data used for the offline training of the clustering models.