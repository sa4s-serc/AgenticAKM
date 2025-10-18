---
### ADR-010: Embed metrics and timestamps in model filenames for versioning

Status: Inferred
Context: Model directories and files encode metrics and timestamps, e.g., 2x256___126.62max__125.87avg__125.12min__1714393719.model and DQN_KO_PEP__...train__...test.model.
Decision: Include run metrics and UNIX timestamps in artifact names to capture performance snapshots and provenance.
Consequences:
- Positive: Immediate visibility of model quality; simplifies selection of best checkpoints; aids reproducibility and auditing.
- Negative: Filenames can become long and unwieldy; potential mismatch between logged metrics and later recalculations; requires consistent naming logic.