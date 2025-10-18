---
### ADR-002: Modular, Algorithm-Centric Code Structure

**Status:** Inferred
**Context:** With the decision to explore multiple Reinforcement Learning algorithms, there was a need to organize the codebase in a way that facilitated experimentation, maintenance, and comparison. A monolithic structure would make it difficult to isolate, debug, or modify individual algorithms without impacting others.

**Decision:** The architecture was designed to be modular, with each RL algorithm implemented in its own distinct Python file (`DQN.py`, `DDPG.py`, `SAC.py`, etc.). This creates a clear separation of concerns, where each file encapsulates the logic, network definitions, and training loop specific to that algorithm.

**Consequences:**
*   **Positive:**
    *   **High Cohesion:** Each file is highly focused on a single algorithm, making the code easier to understand and reason about.
    *   **Low Coupling:** Changes to one algorithm's implementation are unlikely to break another.
    *   **Extensibility:** Adding a new RL algorithm is straightforward—it simply requires creating a new file that adheres to the expected interfaces (likely interacting with `env.py`).
    *   This structure simplifies A/B testing and comparative analysis between different RL approaches.
*   **Negative:**
    *   There may be some code duplication (e.g., replay buffer implementations, network-building utilities) across the different algorithm files if a shared library was not created.
    *   Without strict interface enforcement, the implementations might diverge in subtle ways, making direct comparisons less reliable.