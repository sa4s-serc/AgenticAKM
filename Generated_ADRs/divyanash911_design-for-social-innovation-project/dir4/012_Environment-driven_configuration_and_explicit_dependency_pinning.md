# ADR-012: Environment-driven configuration and explicit dependency pinning

**Date**: 2025-10-13
**Status**: Proposed

## Context
backend/sample.env is provided; backend/requirements.txt and Node package files manage dependencies and scripts.

## Decision
Adopt 12-factor style configuration via environment variables and pin dependencies via requirements and package manifests.

## Consequences
Improves portability and environment parity, but requires secret management and careful dependency updates to avoid drift and vulnerabilities.