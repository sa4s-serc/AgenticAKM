---
### ADR-006: Store and serve uploaded media via the backend public directory

Status: Inferred
Context: The backend uses multer, and there are directories under backend/public (user-images, greddit-images) with static assets. Express typically serves public/ statically.
Decision: Handle file uploads via Multer and store files on the server filesystem under backend/public, serving them as static assets.
Consequences:
- Positive: Simple implementation, fast local development, no external storage dependency.
- Negative: Not horizontally scalable without shared storage; potential disk growth and backup considerations; file path management and security must be handled carefully.