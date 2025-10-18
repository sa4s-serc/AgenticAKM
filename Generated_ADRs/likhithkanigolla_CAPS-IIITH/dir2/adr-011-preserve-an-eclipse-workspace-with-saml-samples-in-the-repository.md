---
### ADR-011: Preserve an Eclipse workspace with SAML samples in the repository

Status: Inferred
Context: SAML-SAMPLE folder includes Eclipse .project/.classpath, .metadata, and multiple sample .capssaml models.
Decision: Commit a working Eclipse workspace containing sample models for reproducibility and reference.
Consequences:
- Positive: Turnkey examples; consistent modeling environment; easier onboarding.
- Negative: Repository bloat; platform-specific artifacts; potential for stale workspace metadata.