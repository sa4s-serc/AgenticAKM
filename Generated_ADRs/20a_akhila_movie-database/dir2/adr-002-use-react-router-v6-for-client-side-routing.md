---
### ADR-002: Use React Router v6 for client-side routing

Status: Inferred
Context: package.json includes react-router-dom@6.0.0-beta.4 and history@^5.0.1. The src/components directory includes route-oriented components like Home, Movie, and NotFound.
Decision: Adopt React Router v6 for handling SPA navigation and route definitions.
Consequences:
- Positive: Modern routing API with better route matching and declarative patterns; smaller bundle than v5 in many cases.
- Negative: Breaking changes from v5; beta version at the time implies potential API instability and the need to adapt to final v6 changes.