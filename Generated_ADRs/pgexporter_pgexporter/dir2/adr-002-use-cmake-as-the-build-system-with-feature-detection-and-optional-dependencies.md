---
### ADR-002: Use CMake as the build system with feature detection and optional dependencies

Status: Inferred
Context: The repo contains CMakeLists.txt at root and various custom Find*.cmake modules (Libev, LibYAML, Lz4, Zstd, Systemd, Check, Libatomic, Pandoc, Pdflatex, Rst2man). Features like compression, TLS, YAML, systemd, and docs are toggled by availability.
Decision: Adopt CMake to orchestrate builds, perform dependency detection, and enable/disable features based on the target environment.
Consequences:
- Positive: Portable builds, granular control of optional features, better integration with IDEs/CI.
- Negative: Additional CMake maintenance; dependency discovery can be fragile across distros.