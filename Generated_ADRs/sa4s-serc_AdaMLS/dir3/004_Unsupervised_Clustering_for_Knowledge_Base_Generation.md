# ADR-004: Unsupervised Clustering for Knowledge Base Generation

**Date**: 2025-10-10
**Status**: Proposed

## Context
A method was required to translate high-dimensional input characteristics (like CPU usage, object count) into a clear adaptation decision (which model to use). Manually defining these rules would be complex, brittle, and not data-driven.

## Decision
Spherical K-Means (SKMeans) clustering, an unsupervised learning technique, was chosen to create the adaptation rules. The offline engine clusters the collected performance data based on input features. Each resulting cluster is then mapped to the single best-performing model for the data points it contains. This mapping constitutes the Knowledge Base.

## Consequences
This automates the creation of a data-driven rule set, making the system more robust and scalable than one with hard-coded logic. The runtime lookup is very efficient (identifying a cluster and retrieving the associated model). However, the system's performance is now critically dependent on the quality of the offline training data and the effectiveness of the clustering algorithm.