---
### ADR-011: Use JSON-based configuration

**Status:** Inferred
**Context:** src/phoenix/config.json is present; there’s no evidence of YAML or .ini configs. Some credentials and tokens are stored as JSON.
**Decision:** Store application configuration in JSON files.
**Consequences:** 
- Positive: Human-readable, widely supported in Python, and easy to parse; consistent with token/credential formats.
- Negative: No built-in comments; environment-specific overrides require external handling; security-sensitive values must be protected.