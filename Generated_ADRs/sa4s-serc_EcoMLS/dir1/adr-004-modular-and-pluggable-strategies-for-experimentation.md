---
### ADR-004: Modular and Pluggable Strategies for Experimentation

**Status:** Inferred
**Context:** The project is a research or experimental system designed to prove the effectiveness of the "EcoMLS" approach. To do this scientifically, the proposed solution must be compared against other, simpler strategies (baselines). A monolithic design would make it difficult to swap out the core decision-making logic for comparison.
**Decision:** The architecture was designed to be modular, allowing for the core analysis and planning logic to be easily replaced. This is evidenced by the parallel directory structures: `EcoMLS/`, `NAIVE1/`, `NAIVE2/`, and `NAIVE3/`. Each of these contains its own implementation of `Analyzer.py` and `Planner.py`, representing a different adaptation strategy. The numerous subdirectories within `Results/` for each strategy confirm that experiments were run by plugging in these different components.
**Consequences:**
*   **Positive:** This structure makes the system highly suitable for experimentation and comparative analysis. It allows researchers to rigorously benchmark different algorithms against each other within the same framework, leading to reproducible results.
*   **Negative:** This approach can lead to code duplication between the different strategy implementations if not carefully managed. The project's file structure is more complex due to the multiple parallel implementations.