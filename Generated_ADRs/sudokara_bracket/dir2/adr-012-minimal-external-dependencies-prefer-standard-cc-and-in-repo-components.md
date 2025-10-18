---
### ADR-012: Minimal external dependencies; prefer standard C/C++ and in-repo components

Status: Inferred
Context: No third-party libraries or submodules are visible; build relies on CMake and standard toolchains. A custom runtime supplies needed language services.
Decision: Keep dependencies minimal by implementing functionality in C/C++ within the repository.
Consequences:
- Positive: Lightweight, portable, easier to build and audit; fewer supply-chain risks.
- Negative: More code to write and maintain; missed opportunities to leverage mature libraries (e.g., parser generators, runtime libraries).