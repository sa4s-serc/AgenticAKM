---
### ADR-005: Tool Use and Safe Code Execution Integration

Status: Inferred
Context: Advanced agents need to call external tools and sometimes execute code to solve tasks (e.g., CodeAct, Python evaluation).
Decision: Introduce Tool and ToolCalls primitives (dspy/adapters/types/tool.py, primitives/Tool, ToolCalls), a PythonInterpreter (primitives/python_interpreter.py) and interoperability with LangChain tools (utils/langchain_tool.py). Provide ReAct and CodeAct modules that orchestrate tool use.
Consequences:
- Positive: Enables complex agent behavior; integrates with existing tool ecosystems; supports code-based reasoning.
- Negative: Security and sandboxing concerns; execution environment management; debugging complexity.