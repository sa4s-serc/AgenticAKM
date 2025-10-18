---
### ADR-009: Train separate clustering models per YOLO size

**Status:** Inferred
**Context:** There are SKMeans model pickles and cluster CSVs for each model size (nano/small/medium/large/xlarge), plus initial centers per size.
**Decision:** Maintain a distinct SKMeans clustering model and initialization for each YOLO variant rather than a single global model.
**Consequences:** 
- Positive: Tailors clusters to each model’s performance profile; potentially better decision boundaries. 
- Negative: Increases storage, training overhead, and complexity in the Planner logic. 
- Trade-off: Accepted operational overhead to gain model-specific precision.