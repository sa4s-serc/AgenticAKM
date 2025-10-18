# ADR-009: Simple collision detection via bounding boxes

**Date**: 2025-10-14
**Status**: Proposed

## Context
Fuel pickups and possibly other interactions need lightweight collision checks.

## Decision
Use axis-aligned bounding boxes to detect overlaps for pickups/collisions.

## Consequences
Fast and easy to implement; may be inaccurate for rotated or elongated shapes and at high speeds; can miss edge cases on curved tracks.