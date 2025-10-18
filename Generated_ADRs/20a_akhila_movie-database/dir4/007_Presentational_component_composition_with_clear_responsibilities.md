# ADR-007: Presentational component composition with clear responsibilities

**Date**: 2025-10-10
**Status**: Proposed

## Context
UI is composed from small reusable components (Header, Grid, Thumb, etc.) with styles split into *.styles.js.

## Decision
Adopt a presentational/logic split and build the UI from small, reusable, styled components.

## Consequences
Improved reuse and maintainability; potential for prop drilling and increased file count, risking over-fragmentation if not managed with patterns or composition.