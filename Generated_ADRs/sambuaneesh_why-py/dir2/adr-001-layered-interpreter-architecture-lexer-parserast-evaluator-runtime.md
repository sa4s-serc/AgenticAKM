### ADR-001: Layered Interpreter Architecture (Lexer → Parser/AST → Evaluator → Runtime)

Status: Inferred
Context: The repository is organized around classic interpreter phases with discrete modules: lexer.py, tok.py, parser.py, ast1.py, eval.py, environment.py, and object.py. Tests exist per layer (lexer_test.py, parser_test.py, eval_test.py), and a REPL/CLI exists (repl.py, main.py).
Decision: Implement a tree-walking interpreter in Python with clear separation of concerns:
- Tokenization in a dedicated lexer (lexer.py, tok.py)
- Parsing into an AST (parser.py, ast1.py)
- Evaluation by walking the AST (eval.py)
- A runtime object model (object.py) and scoped environments (environment.py)
Consequences:
- Positive: High testability and debuggability per layer; educational clarity; easier incremental evolution (e.g., new syntax in parser without touching evaluator logic directly).
- Negative: Slower than bytecode/JIT approaches; potential duplication of logic across layers; more moving parts for small features.