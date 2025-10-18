---
### ADR-010: RESTful API design with layered controllers and routers

Status: Inferred
Context: routes (foodRoute.js, cartRoute.js, orderRoute.js, userRoute.js) and controllers in backend/controllers.
Decision: Expose a REST API organized by resource, mapping routes to controller actions.
Consequences:
- Positive: Conventional structure; easier onboarding; aligns with frontend Axios usage.
- Negative: Versioning and backward compatibility must be planned; might need GraphQL/aggregation endpoints later for complex queries.