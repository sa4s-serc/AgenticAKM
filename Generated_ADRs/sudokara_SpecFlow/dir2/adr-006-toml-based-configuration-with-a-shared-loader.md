---
### ADR-006: TOML-based configuration with a shared loader

Status: Inferred
Context: config.toml exists and there is common/config.py. Both cloud and edge need coordinated parameters (e.g., ports, model IDs, thresholds).
Decision: Store configuration in TOML and provide a shared loader utility in common/config.py so both components read consistent settings.
Consequences:
- Positive: Human-readable, language-agnostic config; a single source of truth; reduces duplication and misconfiguration.
- Negative: Requires robust validation and defaults; configuration changes must be deployed to both sides consistently.