---
### ADR-003: Client-side routing with React Router DOM v7

Status: Inferred
Context: Dependencies include react-router-dom ^7.x in both SPAs, pages/components structure shows routing (e.g., Verify, PlaceOrder, MyOrders).
Decision: Use React Router for SPA navigation and protected routes.
Consequences:
- Positive: Mature routing features; URL-driven navigation; code splitting support.
- Negative: Deep linking and 404 handling requires correct server/static hosting configuration.