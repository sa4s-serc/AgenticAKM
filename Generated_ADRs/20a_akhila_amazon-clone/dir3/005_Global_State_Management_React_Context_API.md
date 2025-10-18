# ADR-005: Global State Management: React Context API

**Date**: 2025-10-10
**Status**: Proposed

## Context
To manage application-wide state, such as the user's authentication status and the contents of the shopping basket, a solution was needed to share data across disparate components without excessive 'prop drilling'.

## Decision
The built-in React Context API was employed for global state management, as evidenced by the `StateProvider` and `reducer` implementation.

## Consequences
This approach avoids adding external state management libraries like Redux, keeping the dependency footprint smaller. It is simpler to implement for small to medium-scale applications. The downside is that it can cause performance issues in very large applications with frequent updates, as any state change in a context will trigger a re-render in all consuming components.