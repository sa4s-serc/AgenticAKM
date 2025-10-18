### ADR-001: Implement pgexporter in C with a minimal runtime footprint

Status: Inferred
Context: The repository is a C codebase with a clear focus on low-level control: custom networking, memory, message handling, and compression modules. It targets Linux distributions and aims to run in server environments where efficiency and control over resources matter.
Decision: Implement the exporter entirely in C to achieve high performance, predictable memory usage, and minimal external dependencies.
Consequences: 
- Positive: High performance, small footprint, fine-grained control over networking and memory, easier static/distro packaging.
- Negative: Higher implementation complexity and maintenance burden; fewer safety nets than managed languages.