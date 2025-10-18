# ADR-009: Asset source-of-truth inconsistency

**Date**: 2025-10-08
**Status**: Proposed

## Context
_site/assets/images includes images not present in the source assets directory.

## Decision
Allow built artifacts to contain assets that are not tracked in the source tree.

## Consequences
Rebuilds may lose untracked assets; provenance becomes unclear; complicates maintenance and PR review; should reconcile assets back into source control.