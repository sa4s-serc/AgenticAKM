# ADR-005: Separation of Concerns for ML and UI Logic

**Date**: 2025-10-10
**Status**: Proposed

## Context
The complex process of running ML inference and rendering results (bounding boxes) on the camera preview involves distinct responsibilities. Intermingling this logic would create a tightly coupled and hard-to-maintain codebase.

## Decision
A clear separation of concerns was established. An `ObjectDetectorHelper.kt` class encapsulates all TFLite-related logic (model loading, pre-processing, inference execution). A separate custom `OverlayView.kt` is dedicated solely to the UI task of rendering bounding boxes and text on the screen.

## Consequences
This design leads to a clean, modular, and testable architecture. The ML inference engine (`ObjectDetectorHelper`) can be updated or replaced without affecting the UI rendering logic, and vice versa. This improves code maintainability and allows for parallel development on different parts of the system.