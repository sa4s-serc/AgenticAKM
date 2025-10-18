---
### ADR-005: Systematic Measurement and Evaluation of the LLM Approach

**Status:** Inferred

**Context:** The introduction of an experimental, non-deterministic LLM-based code generator (ADR-004) raises critical questions about its reliability, correctness, and overall quality compared to the traditional, rule-based approach. To make an informed decision on its viability, its output must be measured and evaluated quantitatively.

**Decision:** To implement a dedicated metrics collection and reporting framework for the LLM-based generator. This is evident from the `llmbased/metrics` directory (with `llm_metrics.py`, `metrics_collector.py`) and the `llmbased/metrics_results` directory, which stores timestamped JSON files of metric data and a summary `metrics_report.md`. This indicates a deliberate effort to systematically assess the performance of the LLM approach.

**Consequences:**
*   **Positive:**
    *   Provides objective, data-driven evidence to compare the LLM and traditional generators.
    *   Allows the team to track progress and regressions as they refine prompts and interact with new LLM versions.
    *   Builds confidence in the LLM-based approach if the metrics demonstrate sufficient quality and reliability.
*   **Negative:**
    *   Adds development and maintenance overhead for the metrics framework itself.
    *   Defining and calculating meaningful metrics for code quality can be complex and subjective.
    *   The process of running evaluations and collecting metrics consumes time and potentially API costs.