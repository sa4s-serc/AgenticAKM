# ADR-010: ADR-010: Secret management and immediate credential hygiene

**Date**: 2025-10-13
**Status**: Proposed

## Context
A plaintext file mongodbatlaspass.txt containing sensitive credentials is committed at the repo root. No .env files are visible.

## Decision
Use environment variables (dotenv for local dev) and never commit secrets. Immediate actions: 1) Remove mongodbatlaspass.txt from the repo, 2) Revoke/rotate leaked MongoDB Atlas credentials, 3) Purge the file from git history with BFG or git filter-repo. Add .env.example files to backend, frontend, and admin documenting required variables. Ensure .gitignore in root and subprojects ignores .env and .env.*. Update code to exclusively read secrets from process.env.

## Consequences
- Eliminates accidental credential disclosure in VCS.
- Requires developers to create local .env from provided examples.
- History rewrite necessitates team coordination (fresh clones/rebases). For production, integrate a managed secrets store when available.