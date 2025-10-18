---
### ADR-007: Configuration management via YAML files with schema validation

Status: Inferred
Context: config/*.yml holds environment/mode-specific settings (default, test, ctf, tutorial, unsafe, etc.). A config.schema.yml exists and lint:config validates it.
Decision: Use YAML-based configuration with schema validation (node-config style) to manage modes and environments.
Consequences:
- Positive: Clear separation of env/mode configs; validation reduces misconfiguration risk; easy overrides.
- Negative: Many config variants add cognitive load; schema must be kept current with code changes.