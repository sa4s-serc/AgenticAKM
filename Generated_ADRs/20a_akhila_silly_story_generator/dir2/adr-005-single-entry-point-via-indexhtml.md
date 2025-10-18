---
### ADR-005: Single entry point via index.html

**Status:** Inferred
**Context:** The naming suggests a single-page entry (index.html) with a single script (index.js). There is no routing configuration or multiple HTML files.
**Decision:** Use index.html as the root document and load application behavior from index.js.
**Consequences:** 
- Positive: Simplified navigation model and deployment, compatible with most static hosts.
- Negative: If client-side routing is needed, it must be implemented manually (e.g., hash-based routes or History API) and may require host configuration for deep links.