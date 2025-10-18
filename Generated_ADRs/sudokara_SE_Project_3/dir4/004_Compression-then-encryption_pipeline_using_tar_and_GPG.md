# ADR-004: Compression-then-encryption pipeline using tar and GPG

**Date**: 2025-10-14
**Status**: Proposed

## Context
Backups must be compact and confidential while remaining interoperable with common tools and easy to restore.

## Decision
Compress artifacts with tar, then optionally encrypt the result using GPG; stage outputs under .phnx/compressed and .phnx/encrypted with timestamped or path-derived names.

## Consequences
Maximizes compression efficacy (encrypt after compress); leverages standard tooling; requires key management; staged artifacts increase local storage footprint and security considerations; restore requires decrypt then untar.