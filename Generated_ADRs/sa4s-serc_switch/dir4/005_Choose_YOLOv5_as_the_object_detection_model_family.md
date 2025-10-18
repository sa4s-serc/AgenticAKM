# ADR-005: Choose YOLOv5 as the object detection model family

**Date**: 2025-10-10
**Status**: Proposed

## Context
The system needs a well-supported detector with multiple capacity variants for adaptive trade-offs.

## Decision
Standardize on YOLOv5 model variants (n/s/m/l/x) for detection across scenarios.

## Consequences
Provides strong community support and clear size–accuracy trade-offs; eases containerization; ties performance characteristics to YOLOv5; extending to other families requires revisiting knowledge/mappings.