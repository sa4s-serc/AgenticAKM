# ADR-014: Client-side result computation for responsiveness

**Date**: 2025-10-13
**Status**: Proposed

## Context
Presence of setResult hook and result_reducer suggests some result aggregation happens in the client.

## Decision
Compute certain questionnaire results client-side to improve immediacy of feedback.

## Consequences
Enhances perceived performance and reduces server load, but computed results should not be treated as authoritative without server validation to prevent tampering.