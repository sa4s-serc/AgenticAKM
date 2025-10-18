---
### ADR-006: Dedicated build stage for libxmljs native module

Status: Inferred
Context: The Dockerfile includes a “libxmljs-builder” stage installing build-essential and python3 to rebuild libxmljs, then copies the compiled module into the distroless runtime.
Decision: Build native dependencies (libxmljs) in a dedicated layer to ensure compatibility with distroless runtime.
Consequences:
- Positive: Enables XML-related features under a secure runtime; avoids runtime build tooling.
- Negative: Increases build complexity and time; potential fragility when upgrading base images or libxmljs.