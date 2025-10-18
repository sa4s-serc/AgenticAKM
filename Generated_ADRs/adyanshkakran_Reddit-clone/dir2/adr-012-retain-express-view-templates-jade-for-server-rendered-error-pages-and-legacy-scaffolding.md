---
### ADR-012: Retain Express view templates (Jade) for server-rendered error pages and legacy scaffolding

Status: Inferred
Context: Backend includes jade as a dependency and views (layout.jade, index.jade, error.jade), typical of express-generator.
Decision: Keep Jade templating for server-rendered pages like error pages while primarily exposing a JSON API for the SPA.
Consequences:
- Positive: Useful default error rendering and diagnostics; minimal extra work given express-generator scaffolding.
- Negative: Mixed paradigms (API + server views) can confuse architecture; additional dependencies for a minor use case.