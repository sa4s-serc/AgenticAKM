---
### ADR-005: Tools as First-Class Plugins with a Registry

Status: Inferred
Context: Agents need to invoke tools/functions (e.g., retrieval, scratchpads) in a controlled, discoverable way. Ad hoc function calls hinder governance and reuse.
Decision: Create a Tool abstraction and ToolRegistry (moya/tools/tool.py, tool_registry.py) with built-in tools like ephemeral_memory.py.
Consequences:
- Positive: Encourages reusable, discoverable, and composable tools; enables governance and validation; simplifies agent-tool integration.
- Negative: Requires metadata discipline; execution safety and resource control must be addressed; registry management adds overhead.