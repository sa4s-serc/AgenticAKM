---
### ADR-010: Centralized Constants

Status: Inferred
Context: Scattered literals and configuration keys increase maintenance risk and inconsistency.
Decision: Centralize shared constants (moya/utils/constants.py).
Consequences:
- Positive: Single source of truth for common values; reduced duplication and typos; easier refactoring.
- Negative: Over-centralization can obscure locality; improper use may create tight coupling on constants.