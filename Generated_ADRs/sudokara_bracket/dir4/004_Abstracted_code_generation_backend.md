# ADR-004: Abstracted code generation backend

**Date**: 2025-10-14
**Status**: Proposed

## Context
The choice of IR/VM is not finalized and the project should remain flexible regarding backend technology.

## Decision
Expose a CodeGen interface without committing to a specific backend (e.g., LLVM) in the current codebase.

## Consequences
Allows swapping in different backends or a custom IR later and keeps front-end development unblocked. Delays backend-specific optimization work and may defer performance validation until a concrete backend is chosen.