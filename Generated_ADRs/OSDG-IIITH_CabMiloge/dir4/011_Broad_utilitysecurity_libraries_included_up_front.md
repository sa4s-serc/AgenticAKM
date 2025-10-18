# ADR-011: Broad utility/security libraries included up front

**Date**: 2025-10-14
**Status**: Proposed

## Context
Dependencies include requests, lxml, dnspython, cryptography, and related low-level packages.

## Decision
Pre-include general-purpose integration and parsing libraries to enable external calls and data processing.

## Consequences
- Ready to integrate with HTTP/XML/DNS/crypto use cases without adding deps later
- Increases image size and attack surface; requires vulnerability scanning and timely updates
- Longer cold-start times in constrained environments
- If unused, pruning improves security posture and performance