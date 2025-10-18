---
### ADR-018: Comprehensive documentation toolchain with man pages and manuals

Status: Inferred
Context: docs include RST manpages, Markdown manuals, and CMake find modules for Pandoc, Pdflatex, Rst2man, Doxygen.
Decision: Maintain extensive documentation generated via a documentation toolchain, covering man pages, manuals, and API references.
Consequences:
- Positive: High-quality, accessible documentation; better UX for operators and developers.
- Negative: Extra build dependencies; documentation maintenance overhead.