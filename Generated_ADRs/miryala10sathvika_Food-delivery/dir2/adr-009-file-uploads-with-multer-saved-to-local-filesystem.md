---
### ADR-009: File uploads with Multer saved to local filesystem

Status: Inferred
Context: multer dependency; backend/uploads directory with food images; admin UI includes image upload affordances.
Decision: Accept image uploads via Multer and store them on the server’s local disk under backend/uploads.
Consequences:
- Positive: Simple implementation; no extra services required; fast local access.
- Negative: Not horizontally scalable without shared storage (e.g., NFS/S3); backup, lifecycle, and CDN concerns; possible disk growth and cleanup needs.