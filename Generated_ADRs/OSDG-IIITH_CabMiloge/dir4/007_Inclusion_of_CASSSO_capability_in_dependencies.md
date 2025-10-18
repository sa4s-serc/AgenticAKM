# ADR-007: Inclusion of CAS/SSO capability in dependencies

**Date**: 2025-10-14
**Status**: Proposed

## Context
python-cas is present in requirements.txt, though actual usage is not confirmed.

## Decision
Provision for Central Authentication Service (CAS) integration by including python-cas.

## Consequences
- Enables institutional SSO if configured later
- Increases image size and supply-chain surface even if unused
- Requires careful configuration and transport security when activated
- If not needed, pruning reduces attack surface and build time