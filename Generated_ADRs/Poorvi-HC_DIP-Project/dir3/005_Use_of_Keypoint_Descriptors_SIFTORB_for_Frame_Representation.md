# ADR-005: Use of Keypoint Descriptors (SIFT/ORB) for Frame Representation

**Date**: 2025-10-14
**Status**: Proposed

## Context
A robust method was needed to quantify the visual similarity between any two frames, resilient to common video variations like changes in scale, rotation, and lighting.

## Decision
The system chose to represent frames using local feature descriptors like SIFT and ORB. These algorithms identify keypoints in each frame and generate a numerical descriptor for each, which can then be efficiently matched to find correspondences and calculate a similarity score.

## Consequences
This technology choice provides a strong foundation for the reconstruction algorithms, as SIFT and ORB are proven to be effective and robust for visual matching tasks. The entire system's performance is fundamentally tied to the descriptive power of these features. While powerful, they may be computationally slower than simpler methods and may not capture global context or semantic information as effectively as modern deep learning-based embeddings.