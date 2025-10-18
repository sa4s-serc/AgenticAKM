---
### ADR-011: Client-side routing with react-router-dom v6

Status: Inferred
Context: Dependency on react-router-dom@^6; multiple dashboard and page components suggest routed views.
Decision: Implement client-side routing using react-router-dom v6.
Consequences:
- Positive: Clean URL-based navigation; code organization by routes; supports role-based route guarding on the client.
- Negative: Requires careful handling of deep links and protected routes; SEO limited vs SSR.