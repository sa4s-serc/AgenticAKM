---
### ADR-009: Provide utilities for drift simulation, dataset ingestion, and model management

Status: Inferred
Context: tools/induce_drift.py, tools/store_pems.py, tools/load_test_models.py, and tools/train_models.py indicate supporting utilities to test robustness, ingest PEMS data, and manage models.
Decision: Include purpose-built tooling for inducing drift, ingesting datasets into MongoDB, and training/loading models to support testing and operational workflows.
Consequences:
- Positive: Improved testability and reproducibility; easier data/model lifecycle management; facilitates scenario-based evaluation.
- Negative: Additional maintenance burden; risk of tool sprawl without strict documentation and standards.