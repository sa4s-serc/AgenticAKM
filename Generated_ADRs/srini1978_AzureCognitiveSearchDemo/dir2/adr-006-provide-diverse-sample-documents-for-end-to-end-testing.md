---
### ADR-006: Provide diverse sample documents for end-to-end testing

**Status:** Inferred
**Context:** The repository includes a sampledocs folder with PDFs, DOCX, PPTX, images, HTML, and text files to simulate real-world content diversity.
**Decision:** Include heterogeneous sample content to validate ingestion, enrichment, and search behavior across formats.
**Consequences:** 
- Positive: Enables realistic testing of the skillset and custom skill; exposes format-specific edge cases (OCR, layout, extraction).
- Negative: Larger repository footprint; potential licensing/redistribution considerations for sample assets.