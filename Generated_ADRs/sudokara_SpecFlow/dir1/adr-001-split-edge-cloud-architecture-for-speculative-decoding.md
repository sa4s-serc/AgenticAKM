### ADR-001: Split Edge-Cloud Architecture for Speculative Decoding

**Status:** Inferred
**Context:** The system needs to run large, computationally expensive AI models (implied by `transformers`, `torch`, `accelerate`) while providing low-latency responses to end-users. Deploying the entire model on an edge device is often infeasible due to resource constraints, while a pure-cloud deployment would suffer from network latency for every interaction. The architectural challenge is to balance model performance and accuracy with responsiveness and deployment flexibility.
**Decision:** The system is designed with a split client-server architecture, separating responsibilities between an "edge" client and a "cloud" server. The project name "Speculative Edge-Cloud Decoding" and the file structure (`edge/client.py`, `edge/draft_model.py` vs. `cloud/server.py`, `cloud/target_model.py`) indicate that a smaller, faster "draft" model runs on the edge for immediate, speculative results, while a larger, more accurate "target" model runs on the cloud for verification and correction.
**Consequences:**
*   **Positive:**
    *   Reduces perceived latency for the end-user by providing instant speculative results from the edge.
    *   Optimizes resource usage by running the heavy computational load on powerful cloud infrastructure.
    *   Reduces the amount of data that needs to be constantly streamed to the cloud, as the edge handles initial processing.
*   **Negative:**
    *   Increases overall system complexity, requiring management of two distinct applications (edge and cloud) and the communication protocol between them (`common/protocol.py`).
    *   Introduces potential consistency challenges between the draft and target models.
    *   Requires a reliable network connection between the edge and the cloud for the verification step.