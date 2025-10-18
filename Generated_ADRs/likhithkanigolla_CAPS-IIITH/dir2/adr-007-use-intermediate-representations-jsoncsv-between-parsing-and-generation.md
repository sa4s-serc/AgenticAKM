---
### ADR-007: Use intermediate representations (JSON/CSV) between parsing and generation

Status: Inferred
Context: Parser modules and sample_output/model.json plus parsed_output.csv indicate a pipeline with intermediate artifacts.
Decision: Normalize parsed SAML into intermediate JSON/CSV representations to decouple parsing from code generation.
Consequences:
- Positive: Clear contracts between stages; easier testing; potential reuse across generators (rule-based and LLM prompts).
- Negative: Extra transformation step; need to version and migrate IR schemas.