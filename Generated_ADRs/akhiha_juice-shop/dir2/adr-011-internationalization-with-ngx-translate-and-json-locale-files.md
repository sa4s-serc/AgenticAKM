---
### ADR-011: Internationalization with ngx-translate and JSON locale files

Status: Inferred
Context: Extensive i18n assets exist in frontend/src/assets/i18n and in data/static/i18n; ngx-translate is a dependency.
Decision: Use ngx-translate with static JSON translation files to support many locales.
Consequences:
- Positive: Broad international reach; straightforward translation workflow; runtime language switching.
- Negative: Large asset footprint; translation maintenance overhead.