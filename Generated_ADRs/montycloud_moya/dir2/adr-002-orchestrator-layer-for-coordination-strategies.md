---
### ADR-002: Orchestrator Layer for Coordination Strategies

Status: Inferred
Context: Different use cases require different agent coordination strategies (single-agent, ReAct-style reasoning, multi-agent collaboration). Hardcoding logic into agents would hinder flexibility and experimentation.
Decision: Define an Orchestrator abstraction (moya/orchestrators/orchestrator.py) with concrete strategies: simple_orchestrator.py, react_orchestrator.py, multi_agent_orchestrator.py.
Consequences:
- Positive: Promotes plug-and-play orchestration strategies; isolates coordination logic; enables algorithmic experimentation without changing agents.
- Negative: Additional complexity and learning curve; potential duplication of cross-cutting concerns across orchestrators (e.g., logging, error handling).