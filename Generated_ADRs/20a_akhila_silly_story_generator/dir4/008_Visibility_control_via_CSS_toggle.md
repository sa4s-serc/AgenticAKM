# ADR-008: Visibility control via CSS toggle

**Date**: 2025-10-10
**Status**: Proposed

## Context
Avoid showing an empty story container before generation.

## Decision
Keep the story paragraph hidden by default using visibility: hidden and reveal it after generation.

## Consequences
Layout space is reserved even when hidden, resulting in stable layout; simple reveal mechanism; initial hidden element remains in the DOM which may require accessibility consideration.