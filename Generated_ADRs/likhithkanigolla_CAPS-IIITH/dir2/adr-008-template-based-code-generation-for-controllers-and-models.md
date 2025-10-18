---
### ADR-008: Template-based code generation for controllers and models

Status: Inferred
Context: Presence of generator/templates/controller_template.py and file_generators indicates template-driven generation.
Decision: Use explicit templates to produce controller/model code from parsed specifications.
Consequences:
- Positive: Consistent, maintainable outputs; easy to review and diff; facilitates customization.
- Negative: Template drift risk if underlying runtime evolves; limited expressiveness for edge cases.