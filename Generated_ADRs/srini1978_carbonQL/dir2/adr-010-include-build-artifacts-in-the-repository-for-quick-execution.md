---
### ADR-010: Include build artifacts in the repository for quick execution

Status: Inferred
Context: The repository contains bin/ and obj/ directories with compiled DLLs and EXE (e.g., carbonQLConsole.exe, carbonQLBackend.dll).
Decision: Check in build outputs to enable immediate execution without a local build step.
Consequences:
- Positive: Speeds up evaluation/demos; useful where build tooling is unavailable.
- Negative: Bloats repository size, risks binary/source divergence, complicates merges; typically discouraged in standard workflows.