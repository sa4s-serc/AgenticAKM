# ADR-010: Multi-backend support including remote agents

**Date**: 2025-10-11
**Status**: Proposed

## Context
Teams may mix cloud, local, and external capabilities and want horizontal scaling.

## Decision
Provide concrete agents for major providers and a RemoteAgent abstraction to call agents over the network with authentication.

## Consequences
Broad portability and deployment flexibility. Expands the testing matrix and introduces network reliability, auth, and version skew concerns for remote calls.