---
### ADR-018: Publish security advisories in CSAF format

Status: Inferred
Context: .well-known/csaf/* contains CSAF provider metadata and advisories.
Decision: Adopt CSAF for publishing security advisories for the project.
Consequences:
- Positive: Standards-based disclosure; easier consumption by security tooling.
- Negative: Requires process to curate and maintain advisories.