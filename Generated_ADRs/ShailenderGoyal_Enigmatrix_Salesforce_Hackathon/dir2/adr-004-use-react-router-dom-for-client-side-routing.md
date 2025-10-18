---
### ADR-004: Use react-router-dom for client-side routing

Status: Inferred
Context: The frontend depends on react-router-dom and has pages under src/pages (Dashboard, Notes, Index, NotFound).
Decision: Implement SPA routing with react-router-dom.
Consequences:
- Positive: Flexible client routing, fast navigation, simple code-splitting options.
- Negative: Requires 404 handling and server fallback configuration; SEO trade-offs typical of SPAs.