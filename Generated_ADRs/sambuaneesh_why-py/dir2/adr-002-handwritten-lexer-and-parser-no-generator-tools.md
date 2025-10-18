---
### ADR-002: Handwritten Lexer and Parser (No Generator Tools)

Status: Inferred
Context: Presence of lexer.py and parser.py without grammars or generator configs suggests a fully hand-rolled frontend. Token definitions in tok.py and AST nodes in ast1.py back this up.
Decision: Build and maintain a custom lexer and parser in Python, with explicit token and AST representations.
Consequences:
- Positive: Full control over parsing strategy and error handling; simplified toolchain; no external parser generator dependencies.
- Negative: Higher maintenance burden; increased risk of subtle parsing bugs; harder to evolve complex grammar features compared to declarative grammars.