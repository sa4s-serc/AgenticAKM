---
### ADR-013: Implement internationalization using resource bundles

Status: Inferred
Context: messages.properties and messages_fr.properties exist in core and agent; Android/web also include localized resources.
Decision: Externalize user-facing strings into locale-specific resource bundles to support multiple languages.
Consequences:
- Positive: Easier localization and community contributions; consistent messaging across modules.
- Negative: Ongoing translation maintenance; ensuring message keys remain consistent across layers.