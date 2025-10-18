---
### ADR-003: Separation of Offline Learning from Online Adaptation

**Status:** Inferred
**Context:** The adaptive system relies on machine learning models to function, but training these models is a computationally expensive and time-consuming process. Performing model training during the system's live operation (online) would consume significant resources, interfering with the primary goal of energy efficiency and introducing unpredictable latency.
**Decision:** The architecture is split into two distinct phases: an offline "Learning Engine" and an online "EcoMLS" adaptation system. The `Learning_Engine/` directory, containing notebooks like `Performance_Evaluator.ipynb` and the individual model data, represents the offline phase where models are trained and evaluated. The core `EcoMLS/` application then uses these pre-trained models for its online, runtime decision-making.
**Consequences:**
*   **Positive:** The online system is lightweight and responsive, as it only needs to perform inference, not training. The expensive learning process does not impact the runtime performance or energy consumption of the operational system.
*   **Negative:** The system's knowledge is static at runtime. It cannot learn from new data or adapt to novel situations that were not present in the offline training data. Updating the system's models requires a full offline retraining and redeployment cycle.