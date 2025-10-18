---
### ADR-008: Enforce code quality with clang-format and clang-tidy

Status: Inferred
Context: .clang-format and .clang-tidy are present at the repository root. The project aims for consistent style and early detection of common issues.
Decision: Standardize formatting and static analysis via clang-format and clang-tidy configurations committed to the repo.
Consequences:
- Positive: Consistent codebase; reduced style churn; automated detection of common pitfalls.
- Negative: Requires developer tooling setup; occasional friction aligning rules with evolving code.