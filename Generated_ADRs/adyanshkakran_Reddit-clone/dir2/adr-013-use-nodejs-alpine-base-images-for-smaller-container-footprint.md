---
### ADR-013: Use Node.js Alpine base images for smaller container footprint

Status: Inferred
Context: All Node-based Dockerfiles use node:alpine as the base.
Decision: Choose node:alpine for backend and frontend containers to minimize image size.
Consequences:
- Positive: Smaller images, faster pulls, lower disk usage.
- Negative: Alpine can have compatibility issues with some native modules; troubleshooting can be slightly more complex.