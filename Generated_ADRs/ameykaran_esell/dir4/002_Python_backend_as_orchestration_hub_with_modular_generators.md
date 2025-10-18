# ADR-002: Python backend as orchestration hub with modular generators

**Date**: 2025-10-14
**Status**: Proposed

## Context
Backend modules include llm.py, infographic_slides.py, visual_overview.py, reel.py, audio.py, utilities, and a single entry point app.py.

## Decision
Structure the backend as an orchestrator (app.py) that delegates to feature-focused modules for each output format.

## Consequences
Pros: high cohesion per feature, easier incremental extension (add new formats), clearer testing per module. Cons: coordination logic in the orchestrator can become complex; requires disciplined interfaces to avoid tight coupling.