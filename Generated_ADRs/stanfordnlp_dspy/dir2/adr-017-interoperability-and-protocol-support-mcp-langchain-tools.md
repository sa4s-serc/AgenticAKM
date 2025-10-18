---
### ADR-017: Interoperability and Protocol Support (MCP, LangChain Tools)

Status: Inferred
Context: Ecosystem interoperability increases adoption and enables richer tool/use-case coverage.
Decision: Add utilities for MCP (utils/mcp.py) and LangChain tool compatibility (utils/langchain_tool.py) to bridge DSPy primitives with external ecosystems.
Consequences:
- Positive: Easier integration with existing stacks; reduced vendor lock-in; broader community reach.
- Negative: Dependency on evolving external protocols; ongoing adapter maintenance; surface area for bugs.