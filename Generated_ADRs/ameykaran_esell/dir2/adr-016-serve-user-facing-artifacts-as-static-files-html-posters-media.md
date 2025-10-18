---
### ADR-016: Serve user-facing artifacts as static files (HTML posters, media)

Status: Inferred
Context: Poster HTML files are generated per user under backend/posters; audio/video outputs stored under backend/video/final_output; frontend components likely fetch these assets.
Decision: Generate and serve user artifacts as static files that the frontend can load directly.
Consequences:
- Positive: Simple delivery path; CDN caching possible; low CPU at request time.
- Negative: Requires file lifecycle management and access control; harder to personalize post-generation without regeneration.