# ADR-001: Adoption of LLVM as the Compiler Backend

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project required a robust and portable way to generate optimized machine code for various target architectures without implementing a code generator and optimizer from scratch.

## Decision
Leverage the LLVM framework as the sole major dependency. The compiler's final stage generates LLVM Intermediate Representation (IR), delegating the concerns of optimization and machine code generation for different platforms to the established LLVM toolchain.

## Consequences
Positive: Drastically reduces development effort by reusing LLVM's powerful optimizers and multi-platform code generators. Provides immediate access to a mature compilation ecosystem. Negative: Introduces a significant external dependency, adding complexity to the build process and tying the project to LLVM's API and release cycle.