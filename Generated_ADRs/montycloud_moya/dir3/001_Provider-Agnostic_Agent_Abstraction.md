# ADR-001: Provider-Agnostic Agent Abstraction

**Date**: 2025-10-11
**Status**: Proposed

## Context
The LLM landscape is fragmented with numerous providers (OpenAI, AWS, local models) and is rapidly evolving. Building a framework tied to a single provider would limit its utility and create vendor lock-in.

## Decision
To define a common `Agent` abstract base class that establishes a consistent interface for all agent implementations. Concrete classes like `OpenAIAgent`, `BedrockAgent`, and `OllamaAgent` then implement this interface for specific backend services.

## Consequences
This pluggable architecture makes the framework highly flexible and future-proof. Developers can easily switch between or combine agents from different providers without rewriting core application logic, preventing vendor lock-in and allowing them to use the best model for the job.