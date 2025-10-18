---
### ADR-011: Hand-written lexer and parser rather than generator tools

Status: Inferred
Context: Custom Lexer.cpp, Parser.cpp, and TokenKinds.* are present; there are no grammar or lexer generator files (e.g., .y/.l). This suggests a hand-written front end.
Decision: Implement a custom lexer and (likely) a recursive-descent parser by hand.
Consequences:
- Positive: Fine-grained control over error recovery and diagnostics; no external generator dependencies; easier embedding.
- Negative: More manual code to maintain; potential for subtle parsing bugs; less automatic tooling support.