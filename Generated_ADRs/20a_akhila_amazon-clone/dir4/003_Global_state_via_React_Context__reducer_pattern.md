# ADR-003: Global state via React Context + reducer pattern

**Date**: 2025-10-10
**Status**: Proposed

## Context
StateProvider.js and reducer.js indicate Context API with a reducer for app-wide state (e.g., cart, user).

## Decision
Manage global state using React Context and a reducer instead of external state libraries.

## Consequences
Lightweight and minimal boilerplate; can cause unnecessary re-renders and performance bottlenecks as state and component tree grow; fewer devtools and ecosystem utilities than Redux/Zustand; more manual structure around side effects.