---
### ADR-008: Precompute detection results per model size as utility inputs

**Status:** Inferred
**Context:** Detection results files per YOLO size exist under “Learning Engine and Adaptation Rules,” used by clustering/rules notebooks and utility plotting.
**Decision:** Use offline detection results as proxies for model utility (e.g., accuracy/latency) when forming adaptation rules.
**Consequences:** 
- Positive: Enables rule derivation without expensive runtime evaluation; consistent benchmarks across runs. 
- Negative: Risk of mismatch with live data or environment variations; may not capture drift. 
- Trade-off: Prefer stable, offline utility estimates over noisy or costly online measurements.