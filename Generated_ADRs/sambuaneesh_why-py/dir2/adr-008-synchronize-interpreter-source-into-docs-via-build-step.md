---
### ADR-008: Synchronize Interpreter Source into Docs via Build Step

Status: Inferred
Context: copy-interpreter.js copies Python interpreter files into documentation/public/interpreter as part of npm run prepare, used by dev/build/CI flows.
Decision: Automatically copy the interpreter source into the docs site’s public assets during build to keep code samples and artifacts in sync.
Consequences:
- Positive: Reduces drift between code and documentation; enables embedding or showcasing current source directly; simplifies demo asset management.
- Negative: Risk of stale copies if the step isn’t run; public exposure of internal files by default; build coupling between Python sources and docs.