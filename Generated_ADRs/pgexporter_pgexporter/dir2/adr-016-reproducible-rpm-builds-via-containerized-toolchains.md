---
### ADR-016: Reproducible RPM builds via containerized toolchains

Status: Inferred
Context: contrib/docker/rpm Dockerfiles and build scripts create an AlmaLinux-based build environment; pgexporter.spec is provided.
Decision: Build RPMs inside containers to ensure reproducible, clean, and dependency-controlled packaging.
Consequences:
- Positive: Consistency across environments; simplified contributor experience; CI-friendly.
- Negative: Requires container tooling; added layer in the build pipeline.