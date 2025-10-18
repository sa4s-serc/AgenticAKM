---
### ADR-006: Use inter-arrival workload features to drive model selection

**Status:** Inferred
**Context:** The presence of resampled_scaled_inter_arrivals.csv and monitor artifacts suggests the workload is characterized via request inter-arrival patterns. Clustering rules are built around such features.
**Decision:** Monitor and use request inter-arrival time features (resampled and scaled) as primary signals for the Analyzer/Planner.
**Consequences:** 
- Positive: Aligns model selection with load dynamics impacting latency/throughput. 
- Negative: May underrepresent other factors (input complexity, accuracy needs) if not incorporated. 
- Trade-off: Prioritized load-sensitive adaptation; may need future extension for content-aware features.