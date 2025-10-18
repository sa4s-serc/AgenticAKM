# ADR-007: Natively Supporting Asynchronous and Streaming Operations

**Date**: 2025-10-13
**Status**: Proposed

## Context
Modern interactive applications, such as chatbots, require responsive, real-time feedback. Traditional blocking API calls to LLMs result in a poor user experience, where the user has to wait for the full response to be generated.

## Decision
Incorporate first-class support for asynchronous operations and streaming outputs, implemented via a simple `dspy.streamify` decorator and support for standards like Server-Sent Events (SSE).

## Consequences
This architectural choice makes DSPy suitable for building production-grade, interactive applications. It dramatically improves the user experience by providing token-by-token output. The trade-off is an increase in the complexity of program state management and control flow for developers using this feature.