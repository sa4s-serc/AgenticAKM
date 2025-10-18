# ADR-004: Performance observability via persistent bottom sheet

**Date**: 2025-10-10
**Status**: Proposed

## Context
info_bottom_sheet.xml exposes real-time metrics (e.g., inference time) with an expand/collapse UI and a Stats/Graphs toggle.

## Decision
Integrate a persistent in-app metrics surface to monitor and debug runtime behavior.

## Consequences
Improves visibility and aids tuning and demos; adds minor UI/runtime overhead and potential clutter if left enabled in production without gating.