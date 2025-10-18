### ADR-001: Adopt a MAPE-K feedback loop for runtime adaptation

**Status:** Inferred
**Context:** The repository is organized into modules named Monitor, Analyzer, Planner, and Execute across two variants (AdaMLS and NAVIE), with a Knowledge directory and artifacts. This mirrors the Monitor-Analyze-Plan-Execute over a shared Knowledge (MAPE-K) reference model for self-adaptive systems.
**Decision:** Implement the system as a MAPE-K loop: Monitor collects runtime signals, Analyzer interprets them, Planner decides adaptations using learned rules and knowledge, and Execute applies changes; knowledge is stored and reused via CSV and pickle artifacts.
**Consequences:** 
- Positive: Clear separation of concerns, easier experimentation, and extensibility of adaptation logic. 
- Negative: Introduces orchestration complexity and potential latency between stages. 
- Trade-off: Opted for architectural clarity and research reproducibility over tightly integrated, lower-latency code paths.