---
### ADR-015: SPA-only rendering (no SSR)

Status: Inferred
Context: Vite + React-only clients; no SSR or server-side rendering framework present; static index.html in both SPAs.
Decision: Serve purely client-rendered SPAs without server-side rendering.
Consequences:
- Positive: Simpler deployment (static hosting for SPAs); reduced server complexity.
- Negative: Initial load/SEO trade-offs; additional work required for crawler-friendly content if needed.