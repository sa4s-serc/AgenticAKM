---
### ADR-013: Provide developer convenience scripts for building and testing

Status: Inferred
Context: make_build.sh and run_tests.sh are provided alongside CMake and Python test drivers.
Decision: Ship simple shell scripts to streamline common developer workflows for building and running the full test suite.
Consequences:
- Positive: Lower barrier to entry; consistent local workflows; quicker iteration.
- Negative: Potential duplication with CMake/CI; scripts may bitrot across environments or shells.