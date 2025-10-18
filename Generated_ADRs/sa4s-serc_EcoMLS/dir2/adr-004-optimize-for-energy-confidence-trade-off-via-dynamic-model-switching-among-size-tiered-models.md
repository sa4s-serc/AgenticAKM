---
### ADR-004: Optimize for energy-confidence trade-off via dynamic model switching among size-tiered models

Status: Inferred
Context: Learning_Engine/individual_model contains nano/small/med/large CSVs; Results include “Energy_vs_Confidence_*” plots and “Model Switching Plot”; EcoMLS/model.csv suggests model metadata.
Decision: Maintain multiple model variants (nano/small/med/large) and dynamically switch among them to balance energy consumption and inference confidence.
Consequences:
- Positive: Enables energy savings while preserving acceptable confidence; supports adaptive optimization.
- Negative: Switching incurs overhead; requires accurate confidence/energy estimation; potential instability if oscillations occur.