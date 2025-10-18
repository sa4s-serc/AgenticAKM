---
### ADR-005: Provide two pipelines: adaptive (AdaMLS) and baseline (NAVIE)

**Status:** Inferred
**Context:** The repository has parallel directories AdaMLS and NAVIE, each with Monitor/Analyzer/Planner/Execute modules and separate logs; Results include logs for both.
**Decision:** Implement both an adaptive pipeline (AdaMLS) and a baseline (NAVIE) to enable side-by-side evaluation.
**Consequences:** 
- Positive: Enables empirical comparison and ablation studies; clarifies benefits of adaptation. 
- Negative: Duplicates code structure and increases maintenance overhead. 
- Trade-off: Accepted duplication to ensure fair, controlled comparisons.