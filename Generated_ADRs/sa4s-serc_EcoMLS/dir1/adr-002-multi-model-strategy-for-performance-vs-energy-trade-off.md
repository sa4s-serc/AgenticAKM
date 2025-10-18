---
### ADR-002: Multi-Model Strategy for Performance vs. Energy Trade-off

**Status:** Inferred
**Context:** The system needs to balance two conflicting goals: performance (implied by "Confidence" in result plots) and energy consumption. Using a single, monolithic Machine Learning model would provide a static trade-off, unable to adapt to changing workloads or energy constraints. The system required a mechanism to dynamically shift its position on the performance-energy spectrum.
**Decision:** A portfolio of pre-trained Machine Learning models of varying sizes and complexities was adopted. This is evident from the `Learning_Engine/individual_model/` directory, which contains data or models named `nano.csv`, `small.csv`, `med.csv`, and `large.csv`. The `Planner.py` and `Analyzer.py` components likely use system metrics to decide which of these models to activate. Result plots like "Model Switching Plot.drawio.pdf" and "Energy vs Confidence" confirm this dynamic switching behavior.
**Consequences:**
*   **Positive:** The system gains significant flexibility. It can operate in a low-power, lower-performance mode by using the "nano" or "small" model, and switch to a high-power, high-performance mode with the "large" model when needed. This allows for fine-grained optimization of the energy-performance trade-off at runtime.
*   **Negative:** This approach increases storage requirements, as multiple models must be available to the system. It also adds complexity to the "Planner" component, which now must contain the logic to select the optimal model based on current conditions.