---
### ADR-012: Architecture documentation as code with PlantUML

Status: Inferred
Context: The repository contains multiple .puml files (e.g., RssReaderFinal.puml, CyclicLater.puml) and corresponding PNGs, indicating model-driven diagrams kept in version control.
Decision: Maintain architecture diagrams using PlantUML and commit both source (.puml) and rendered images.
Consequences:
- Positive: Versioned, reviewable architecture documentation; easy to regenerate and update.
- Negative: Requires discipline to keep images in sync with .puml; additional tooling for rendering.