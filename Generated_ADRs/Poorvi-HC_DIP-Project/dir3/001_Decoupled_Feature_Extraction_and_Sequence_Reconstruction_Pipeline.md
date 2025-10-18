# ADR-001: Decoupled Feature Extraction and Sequence Reconstruction Pipeline

**Date**: 2025-10-14
**Status**: Proposed

## Context
The core task of reordering shuffled video frames requires intensive comparison between frames. Performing this comparison on raw pixel data repeatedly for every algorithm would be computationally prohibitive and inefficient.

## Decision
A two-stage pipeline was implemented. A dedicated script (`extract_features.py`) first preprocesses all video frames to extract and persist robust visual features (like SIFT descriptors). Subsequent reconstruction algorithms then operate on these pre-computed features, not the raw video.

## Consequences
This decoupling significantly improves performance by ensuring the expensive feature extraction step is run only once. It enables rapid experimentation with different reconstruction algorithms and promotes modularity by creating a clear separation of concerns between feature representation and sequencing logic. However, the overall system's success becomes critically dependent on the quality of the features chosen in the first stage.