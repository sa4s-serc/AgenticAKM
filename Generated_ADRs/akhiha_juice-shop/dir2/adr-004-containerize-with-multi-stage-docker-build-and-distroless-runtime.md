---
### ADR-004: Containerize with multi-stage Docker build and distroless runtime

Status: Inferred
Context: The Dockerfile uses node:20-buster for install/build and gcr.io/distroless/nodejs20-debian11 for runtime. It sets non-root user (65532), manipulates permissions (g=u), and prunes artifacts for minimal image size.
Decision: Use a multi-stage build producing a small, secure, distroless runtime image running as a non-root user; apply OpenShift-friendly permissions (group 0, g=u).
Consequences:
- Positive: Reduced attack surface; smaller images; improved runtime security and platform compatibility.
- Negative: Debugging is harder (no shell); native module handling becomes more complex; more advanced Dockerfile.