---
### ADR-002: Strategy Pattern for Agent Orchestration Logic

**Status:** Inferred
**Context:** An agent or a group of agents can be coordinated in multiple ways to solve a problem. A simple task might only require a single request-response cycle. A more complex task might need a multi-agent collaboration, while another might benefit from a structured reasoning-and-action loop (like ReAct). A single, monolithic control flow would not be able to accommodate these varied interaction patterns efficiently.

**Decision:** The agent coordination logic was separated into distinct "Orchestrator" strategies. A base `Orchestrator` class (`moya/orchestrators/orchestrator.py`) defines a standard execution contract. Different concrete strategies are then implemented to handle specific coordination patterns, as seen in `SimpleOrchestrator`, `MultiAgentOrchestrator`, and `ReActOrchestrator`. The application can select and use the appropriate orchestrator strategy based on the task's requirements.

**Consequences:**
*   **Positive:**
    *   **Algorithmic Flexibility:** It is easy to add new, sophisticated agent coordination algorithms (e.g., new planning or collaboration techniques) by simply adding a new orchestrator class.
    *   **Separation of Concerns:** The core agent capabilities (LLM interaction, tool use) are kept separate from the high-level logic that coordinates them.
    *   **Reusability:** The same set of agents and tools can be used under different orchestration strategies to solve different kinds of problems.
*   **Negative:**
    *   **Configuration Complexity:** Users of the framework must understand the different orchestrators and choose the correct one for their use case, which can increase the initial learning curve.
    *   **State Management:** State management can become more complex as it may need to be passed between or handled differently by various orchestrator strategies.