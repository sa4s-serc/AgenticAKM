---
### ADR-012: Dataclass-driven configuration and typed domain models

Status: Inferred
Context: config/ includes flat_dataclass.py, base_poly_config.py, utils.py, YAML configs; core/datatypes defines typed entities (sequence, sampling_params, scheduler_output, step_inputs, request_output).
Decision: Use Python dataclasses and polymorphic configs (with YAML) to configure engines, benchmarks, and policies; represent runtime entities with strongly-typed dataclasses.
Consequences:
- Positive: Safer refactoring; clearer contracts across components; easier serialization and validation.
- Negative: Potential friction when integrating dynamic configs; need to maintain schema evolution.