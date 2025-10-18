# ADR-011: ADR-011: VCS policy for runtime artifacts, build outputs, and sensitive files

**Date**: 2025-10-13
**Status**: Proposed

## Context
backend/uploads is currently tracked; sensitive file mongodbatlaspass.txt was committed; typical generated artifacts are not needed in source control.

## Decision
Do not commit runtime artifacts or generated files. Update .gitignore at root and in subprojects to exclude: backend/uploads, node_modules/, dist/, build/, .vite/, logs/, coverage/, .env, .env.*, and editor/OS files. Immediate actions: remove currently tracked artifacts with git rm -r --cached backend/uploads; commit the changes; add ignores; purge large/sensitive files from history if needed (coordinate with ADR-010 for secrets).

## Consequences
- Smaller, safer repository and faster clones.
- Developers must manage local runtime data via scripts or fixtures.
- CI/CD must build artifacts and fetch uploads from storage (see ADR-006) rather than relying on Git.