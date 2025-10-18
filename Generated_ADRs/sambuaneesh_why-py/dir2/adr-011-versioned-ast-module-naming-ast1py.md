---
### ADR-011: Versioned AST Module Naming (ast1.py)

Status: Inferred
Context: The AST module is named ast1.py, implying potential future versions or experimental AST shapes.
Decision: Name the AST module with a version suffix to allow parallel evolution of AST representations without breaking existing code.
Consequences:
- Positive: Enables experimentation and incremental redesigns of the AST; smoother migrations; supports research/report workflows.
- Negative: Potential confusion over which AST version is active; duplication risk; added maintenance if multiple ASTs co-exist.