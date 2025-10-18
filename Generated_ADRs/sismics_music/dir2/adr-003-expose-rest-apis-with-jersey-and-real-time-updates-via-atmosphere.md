---
### ADR-003: Expose REST APIs with Jersey and real-time updates via Atmosphere

Status: Inferred
Context: music-web depends on Jersey (jersey-container-servlet, json-processing, multipart) and Atmosphere runtime. Resources implement REST endpoints (e.g., AlbumResource, TrackResource, PlayerResource), and an Atmosphere-based PlayerResource exists for push events.
Decision: Build HTTP APIs using Jersey (JAX-RS) and enable real-time client updates (player state, etc.) using Atmosphere (WebSocket/Comet).
Consequences:
- Positive: Standards-based REST; mature ecosystem; Atmosphere abstracts transport for broad client compatibility.
- Negative: Additional operational complexity (WebSocket lifecycles, scaling considerations); Atmosphere adds a dependency surface and server resource management needs.