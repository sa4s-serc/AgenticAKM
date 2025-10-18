# ADR-009: Mixed UI library strategy (MUI + Bootstrap + others)

**Date**: 2025-10-10
**Status**: Proposed

## Context
Dependencies include @mui/material, @mui/icons-material, @emotion/*, bootstrap, react-bootstrap, and multiple carousel/slider libraries.

## Decision
Allow multiple UI/tooling libraries in the same app to accelerate development of different features.

## Consequences
Rapid prototyping with rich components; increased CSS/JS payload and potential runtime conflicts; inconsistent look-and-feel; more complicated theming and accessibility alignment across libraries; harder long-term maintenance.