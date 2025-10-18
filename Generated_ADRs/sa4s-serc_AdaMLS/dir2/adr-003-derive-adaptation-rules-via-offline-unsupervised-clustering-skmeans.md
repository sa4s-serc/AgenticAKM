---
### ADR-003: Derive adaptation rules via offline unsupervised clustering (SKMeans)

**Status:** Inferred
**Context:** The “Learning Engine and Adaptation Rules” contains notebooks for selecting K, SKMeans models and initial centers per size, and cluster CSVs. Knowledge_get_cluster includes mapping CSVs for each YOLO variant.
**Decision:** Use offline SKMeans clustering to learn workload/utility structure and generate adaptation rules and cluster mappings that guide runtime planning.
**Consequences:** 
- Positive: Reduces runtime computation; rules are explainable and lightweight to apply. 
- Negative: Requires periodic retraining and may suffer from concept drift if workload changes. 
- Trade-off: Favor offline learning with simple runtime inference over continuous online learning complexity.