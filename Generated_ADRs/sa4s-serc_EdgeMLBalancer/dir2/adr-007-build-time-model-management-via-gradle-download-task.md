---
### ADR-007: Build-time model management via Gradle download task

Status: Inferred
Context: The project applies the de.undercouch.download plugin and includes download_models.gradle; comments indicate default model download during build with the option to place custom models in assets.
Decision: Provide a Gradle task to fetch default models at build time while supporting manual asset placement for custom models.
Consequences:
- Positive: Smooth project bootstrap for contributors; reproducible builds with known model versions.
- Negative: Build-time network dependency when downloading; must manage version pins and cache; potential duplication with already-bundled assets.