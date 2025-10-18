# ADR-010: Multi-Package-Manager Distribution

**Date**: 2025-10-14
**Status**: Proposed

## Context
The iOS ecosystem uses multiple dependency managers across codebases and CI pipelines.

## Decision
Publish and maintain support for Swift Package Manager, CocoaPods, and Carthage with appropriate manifests and automation.

## Consequences
Pros: Maximizes adoption, fits diverse build systems, reproducible dependency resolution. Cons: Higher release and CI complexity, version pinning and integration issues across managers, extra maintenance overhead.