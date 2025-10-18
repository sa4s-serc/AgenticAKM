# ADR-006: Global state via React Contexts instead of Redux

**Date**: 2025-10-16
**Status**: Proposed

## Context
The app uses AuthContext, LearningContext, and ThemeContext for cross-cutting client state.

## Decision
Rely on React Context providers for global state rather than introducing Redux/MobX.

## Consequences
Lower complexity and boilerplate; risk of unnecessary re-renders and scalability issues as state grows; may need selectors or context splitting if contexts expand.