# ADR-007: Visual learning path builder as a first-class module

**Date**: 2025-10-16
**Status**: Proposed

## Context
Adaptive learning is central to the product and benefits from an interactive pathway editor.

## Decision
Ship a custom VisualLearningPath editor and node-based view for composing learning paths.

## Consequences
Differentiated UX and adaptability; increases front-end complexity and necessitates robust persistence/versioning on the backend; opens door to future collaborative editing and analytics.