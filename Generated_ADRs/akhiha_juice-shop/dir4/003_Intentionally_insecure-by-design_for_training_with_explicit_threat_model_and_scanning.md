# ADR-003: Intentionally insecure-by-design for training, with explicit threat model and scanning

**Date**: 2025-10-10
**Status**: Proposed

## Context
Core purpose is to teach web security by embedding exploitable scenarios while still running in public CI and community environments.

## Decision
Deliberately include vulnerabilities and challenge artifacts, maintain threat-model.json, and run OWASP ZAP and other scanners in CI to prevent accidental hardening that would break training content.

## Consequences
Benefits: realistic, reproducible security exercises; durable challenge stability. Drawbacks: must not be deployed as-is to production; requires strong documentation and isolation; security tooling needs tuning to allow intended vulns.