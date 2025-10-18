---
### ADR-003: AST-Centric Design With Tree-Walking Evaluation

Status: Inferred
Context: The existence of ast1.py and eval.py indicates evaluation proceeds by traversing AST nodes produced by the parser, rather than compiling to bytecode or another IR/VM.
Decision: Use a tree-walking evaluator that interprets AST nodes directly at runtime.
Consequences:
- Positive: Easy to reason about; straightforward mapping from syntax to semantics; fast iteration for language features.
- Negative: Performance penalties for repeated traversals; harder to implement optimizations (constant folding, inlining) compared to an IR/bytecode VM.