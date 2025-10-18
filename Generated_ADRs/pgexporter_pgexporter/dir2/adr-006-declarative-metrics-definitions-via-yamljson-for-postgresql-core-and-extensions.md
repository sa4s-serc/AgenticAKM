---
### ADR-006: Declarative metrics definitions via YAML/JSON for PostgreSQL core and extensions

Status: Inferred
Context: contrib/yaml and contrib/json contain per-PostgreSQL-version metric definitions; extensions/*.yaml define extension-specific metrics; docs JSON.md and YAML.md describe the formats.
Decision: Use declarative YAML/JSON files to define metrics and queries per PostgreSQL version and per extension, loaded at runtime.
Consequences:
- Positive: Extensible without recompilation; easier community contributions; decouples code from query definitions.
- Negative: Requires robust parsers/validators; runtime errors if definitions are malformed; managing version matrices can be complex.