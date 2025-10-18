# ADR-002: Custom client–server protocol layer

**Date**: 2025-10-14
**Status**: Proposed

## Context
Reliable, low-overhead messaging between edge and cloud is required for token proposal/verification cycles.

## Decision
Implement a bespoke protocol and message schema in common/protocol.py rather than using off-the-shelf RPC frameworks.

## Consequences
Gives fine-grained control over payloads and performance; increases burden for validation, versioning, compatibility, security hardening, and tooling compared to gRPC/HTTP standards.