# ADR-006: Domain-oriented routing and UI structure

**Date**: 2025-10-14
**Status**: Proposed

## Context
Backend routes include user, greddit, post, and report; frontend routes reflect similar domains (mysubs, reports, requests, stats, savedposts, profile).

## Decision
Organize both API endpoints and frontend pages around core domain entities and workflows rather than technical layers.

## Consequences
Improves clarity and modularity, aligns teams around features, and eases evolution of domain capabilities; risks tight coupling between frontend and backend contracts and requires consistent cross-cutting policies (auth, validation) across domains.