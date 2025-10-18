---
### ADR-006: Golden-file test suite organized by feature with expected .out/.err and optional .in

Status: Inferred
Context: The tests directory contains .rkt programs grouped by features (if, int, loops, var, functions, vector, static_type) with corresponding .out, .err, and occasionally .in files. Python scripts and shell runners orchestrate these tests.
Decision: Adopt golden-file testing: compile and run programs, compare stdout/stderr with expected files, and provide input via .in when needed.
Consequences:
- Positive: Clear specification of expected behavior; good regression detection; tests double as documentation.
- Negative: Output format changes require updating many files; tests can be brittle; full end-to-end runs may be slower.