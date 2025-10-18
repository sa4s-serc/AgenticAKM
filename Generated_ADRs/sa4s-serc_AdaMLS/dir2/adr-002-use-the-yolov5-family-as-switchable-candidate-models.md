---
### ADR-002: Use the YOLOv5 family as switchable candidate models

**Status:** Inferred
**Context:** The knowledge and results refer to YOLOv5 variants (nano, small, medium, large, xlarge) with detection results per size. The system logs switching behavior and utility, implying runtime selection among these variants.
**Decision:** Treat YOLOv5n/s/m/l/x as the candidate set for dynamic model selection/switching at runtime.
**Consequences:** 
- Positive: Provides a spectrum of latency/accuracy trade-offs for adaptation. 
- Negative: Ties the adaptation to a specific model family and its deployment constraints. 
- Trade-off: Gains practical, well-understood choices at the expense of generality to other model families.