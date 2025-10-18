---
### ADR-004: Decoupled Experiment Tracking and Visualization

**Status:** Inferred
**Context:** Training and evaluating RL agents is an iterative and data-intensive process. It is critical to log metrics, track experiment configurations, and visualize results to understand agent performance, debug issues, and compare different runs. These monitoring and analysis tasks should not be tightly coupled with the core training logic.

**Decision:** A dedicated and decoupled system for logging and visualization was established.
1.  **Logging:** TensorBoard was chosen as the primary tool for logging training metrics, indicated by the numerous `events.out.tfevents` files in the `logs/` directory. The structured log directory names (`2x256-17149...`, `DQN_KO_PEP-17150...`) show a systematic way of organizing experiments.
2.  **Artifact Storage:** Raw reward data and summary statistics are stored in CSV files (`rewards/.../..._rewards.csv`, `stats.csv`).
3.  **Visualization:** Final plots are generated and saved as image files (`rewards/.../KO_PEP.png`), likely by a dedicated script (`plot.py`).

**Consequences:**
*   **Positive:**
    *   **Separation of Concerns:** The core RL algorithm code is kept clean of verbose logging and plotting logic.
    *   **Standardization:** Using TensorBoard provides a powerful, industry-standard interface for real-time visualization of training progress.
    *   **Persistence and Reproducibility:** Saving raw data in CSVs and final plots as images ensures that results are preserved and can be analyzed offline, long after the experiment has finished.
*   **Negative:**
    *   The system relies on multiple formats and locations for its outputs (TensorBoard logs, CSV files, PNG images), which might require developers to look in several places to get a complete picture of an experiment's outcome.
    *   Requires developers to be familiar with the TensorBoard interface and potentially other plotting libraries used in `plot.py`.