# ADR-007: ADR-007: Separate admin SPA and deployment surface

**Date**: 2025-10-13
**Status**: Proposed

## Context
The admin app (admin/) provides pages for Add, List, and Orders, distinct from the customer-facing frontend.

## Decision
Keep the admin interface as a separate SPA and deployment target with its own base URL and credentials/roles. Enforce admin-only access at both UI and API levels.

## Consequences
- Operational concerns and workflows are isolated from the customer experience.
- Independent release cadence and access controls.
- Some duplication of shared UI; consider a shared component library later if warranted.