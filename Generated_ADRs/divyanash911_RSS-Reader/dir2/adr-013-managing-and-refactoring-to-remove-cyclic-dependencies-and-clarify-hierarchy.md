---
### ADR-013: Managing and refactoring to remove cyclic dependencies and clarify hierarchy

Status: Inferred
Context: Diagram assets include names like Removedcyclic.png, CyclicLater.puml, AddedHierarchy.png, Refactored_Tree_wide.png, and WideHierarchy.png, suggesting a concerted effort to restructure dependencies.
Decision: Refactor the codebase to eliminate cyclic dependencies and establish a clearer, wider hierarchical structure between components.
Consequences:
- Positive: Improved modularity, testability, and maintainability; reduced build-order issues; clearer ownership and boundaries.
- Negative: Short-term refactor cost; potential impact on existing integrations; requires ongoing governance to prevent regressions.