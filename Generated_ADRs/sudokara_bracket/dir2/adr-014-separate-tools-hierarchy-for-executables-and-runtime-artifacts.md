---
### ADR-014: Separate tools/ hierarchy for executables and runtime artifacts

Status: Inferred
Context: tools/ contains driver/ for the CLI and runtime/ for the C runtime, each with their own CMakeLists, clearly separating them from the core library in lib/.
Decision: Organize executables and runtime under tools/ to keep core library code isolated and to clarify build targets.
Consequences:
- Positive: Cleaner repository structure; clearer ownership and dependencies; easier packaging of tools versus libraries.
- Negative: Requires cross-directory coordination in the build; potential duplication of configuration across CMake files.