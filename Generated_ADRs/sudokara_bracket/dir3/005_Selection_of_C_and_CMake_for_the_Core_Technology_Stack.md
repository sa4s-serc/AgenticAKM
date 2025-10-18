# ADR-005: Selection of C++ and CMake for the Core Technology Stack

**Date**: 2025-10-14
**Status**: Proposed

## Context
A high-performance, systems-level programming language with a robust, cross-platform build system was required to build the compiler and interface directly with the C++-based LLVM libraries.

## Decision
The entire compiler was implemented in C++. The build process is managed by CMake to handle dependencies, library linkage, and cross-platform compatibility.

## Consequences
Positive: C++ offers the performance necessary for a compiler and provides seamless, first-class interoperability with the LLVM framework's C++ APIs. CMake is the industry standard for such projects. Negative: C++ has a steep learning curve and requires careful memory management, increasing development complexity and the potential for bugs compared to higher-level languages.