# ADR-002: MkDocs as the documentation stack

**Date**: 2025-10-13
**Status**: Proposed

## Context
Docs are under docs/ with mkdocs.yml, requirements.txt, Pipfile, and Vercel configuration.

## Decision
Use MkDocs to build a static documentation portal for guides and API references.

## Consequences
Pros: fast static site, easy theming, simple CI/CD. Cons: less native support for auto API extraction vs Sphinx, requires explicit syncing when code lives elsewhere.