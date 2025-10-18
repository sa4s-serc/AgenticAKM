# ADR-010: Heterogeneous Sample Documents for End-to-End Validation

**Date**: 2025-10-09
**Status**: Proposed

## Context
Sampledocs includes varied file types (PDF, DOCX, HTML, images, PPTX, TXT) for testing content ingestion and enrichment.

## Decision
Provide a diverse corpus to exercise indexers, extractors, and the custom skill in realistic scenarios.

## Consequences
Accelerates local validation and demos, exposes encoding/format edge cases early, but increases repo size and may require guidance on expected extraction behavior; not a substitute for formal test suites.