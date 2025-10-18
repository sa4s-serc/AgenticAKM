---
### ADR-005: Provide a REPL and CLI Entry Points

Status: Inferred
Context: repl.py and main.py exist alongside eval.py and parser.py, suggesting interactive and script-execution modes.
Decision: Offer an interactive REPL and a command-line driver for running programs.
Consequences:
- Positive: Improves developer ergonomics; supports experimentation and learning; facilitates quick feedback loops during development.
- Negative: Requires maintenance of interaction layer and error reporting UX; adds surface area for testing and packaging.