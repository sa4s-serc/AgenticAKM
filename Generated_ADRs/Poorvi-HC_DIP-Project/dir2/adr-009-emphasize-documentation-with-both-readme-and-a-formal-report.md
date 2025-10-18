---
### ADR-009: Emphasize documentation with both README and a formal report

Status: Inferred
Context: README.md and Video Reconstruction Report.pdf are included, indicating a decision to retain narrative and formal documentation alongside code.
Decision: Store high-level documentation and a detailed report within the repository to capture methodology and findings.
Consequences:
- Positive: Improves knowledge transfer, reproducibility context, and stakeholder communication.
- Negative: Storing binary PDFs in VCS increases repo size and can complicate diffs; requires diligence to keep docs synchronized with code changes.