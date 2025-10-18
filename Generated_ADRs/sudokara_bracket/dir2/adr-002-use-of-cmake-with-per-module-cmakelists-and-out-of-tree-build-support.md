---
### ADR-002: Use of CMake with per-module CMakeLists and out-of-tree build support

Status: Inferred
Context: The project contains CMakeLists.txt at the root and under lib/*, tools/*, tests/, and tools/runtime. Scripts (make_build.sh) suggest automated out-of-tree builds. The project needs to build mixed C/C++ code and separate tools and libraries.
Decision: Use CMake as the build system with modular CMakeLists in each component, enabling cross-platform builds and easy integration of tests and tools.
Consequences:
- Positive: Portability, good IDE/tooling support, modular builds, and easier integration of C and C++ targets.
- Negative: CMake complexity and learning curve; duplication of simple build steps versus plain Make.