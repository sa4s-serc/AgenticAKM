---
### ADR-006: Strong Unit Testing at Each Interpreter Layer

Status: Inferred
Context: lexer_test.py, parser_test.py, and eval_test.py indicate a strategy of testing per subsystem.
Decision: Maintain focused unit tests for lexer, parser, and evaluator to ensure correctness and regressions are caught early.
Consequences:
- Positive: High confidence in changes; easier debugging and refactoring; enables safe evolution of the language.
- Negative: Additional upfront investment to write and maintain tests; may slow initial feature spikes.