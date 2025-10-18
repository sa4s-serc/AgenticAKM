---
### ADR-012: Include external media ingestion via youtube-dl/yt-dlp

Status: Inferred
Context: Dockerfile installs yt-dlp as youtube-dl; the web UI includes an “AddExternal” controller; import services exist server-side.
Decision: Support importing external media sources (e.g., online videos) by bundling youtube-dl/yt-dlp in server distributions and wiring it into import flows.
Consequences:
- Positive: Expands content sources; user convenience for bringing external tracks into the library.
- Negative: Legal/licensing considerations depending on source; dependency on external tool behavior and frequent updates; potential breakage when sites change.