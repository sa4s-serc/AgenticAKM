# ADR-007: Authentication via Google OAuth

**Date**: 2025-10-13
**Status**: Proposed

## Context
Dependency management includes Google OAuth libraries.

## Decision
Provide OAuth-based authentication using Google as an identity provider.

## Consequences
Simplifies user login and offloads credential storage; reduces custom auth maintenance; excludes users without Google accounts unless alternative auth paths exist; requires secure handling of OAuth secrets and callbacks.