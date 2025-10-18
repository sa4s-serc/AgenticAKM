---
### ADR-002: Structured and Multi-Modal I/O via Adapters

Status: Inferred
Context: LMs emit unstructured text by default, yet applications require structured, typed, and multi-modal inputs/outputs (e.g., JSON, XML, tool calls, images, audio).
Decision: Implement an Adapter layer (dspy/adapters) with ChatAdapter, JSONAdapter, XMLAdapter, TwoStepAdapter, and a type system (adapters/types: audio, image, code, tool, citation, history, document). Provide utilities and validation around these adapters.
Consequences:
- Positive: More reliable parsing; support for complex/multi-modal exchanges; better contract-driven prompts; improved evaluation fidelity.
- Negative: Increased complexity; stricter contracts can increase failure modes if prompts drift; overhead in adapter maintenance and error handling.