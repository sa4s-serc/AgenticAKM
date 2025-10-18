# ADR-014: Operational model favors script-based long-running tasks

**Date**: 2025-10-14
**Status**: Proposed

## Context
Video processing and LLM batch steps are implemented as Python scripts (run.py, run.sh) without explicit queue/workers.

## Decision
Execute long-running processing via scripts invoked from the backend or manually, rather than through a job queue.

## Consequences
Pros: fast to implement, easy local runs. Cons: API responsiveness risks under load, harder failure recovery and scaling; likely needs migration to background workers for production.