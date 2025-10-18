# ADR-005: Dedicated Support for Reactive Programming Paradigms

**Date**: 2025-10-14
**Status**: Proposed

## Context
Modern Swift development increasingly relies on asynchronous programming paradigms like Combine and RxSwift for managing complex event streams and data flows, especially for network responses. A traditional callback-based API would not integrate well with these modern architectures.

## Decision
To provide dedicated, first-class integration modules for major reactive frameworks, including Combine, RxSwift, and ReactiveSwift. This allows network responses to be returned as reactive signals or publishers.

## Consequences
Moya seamlessly integrates into modern, reactive application architectures. This provides developers with an elegant and declarative way to handle network responses, chaining, and error management, catering to advanced use cases and improving code readability.