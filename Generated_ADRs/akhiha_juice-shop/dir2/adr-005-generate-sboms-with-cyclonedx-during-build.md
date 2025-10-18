---
### ADR-005: Generate SBOMs with CycloneDX during build

Status: Inferred
Context: The Dockerfile installs @cyclonedx/cyclonedx-npm and runs npm run sbom; the frontend uses @cyclonedx/webpack-plugin.
Decision: Produce CycloneDX SBOMs for transparency and supply chain security for both backend and frontend.
Consequences:
- Positive: Better dependency visibility; facilitates compliance and vulnerability management.
- Negative: Adds build time and tooling complexity.