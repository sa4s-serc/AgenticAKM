# ADR-001: React 18 SPA with Redux Toolkit and React Router

**Date**: 2025-10-13
**Status**: Proposed

## Context
The frontend under code/src is a React app and the lockfile shows React 18, Redux Toolkit, and React Router.

## Decision
Build a single-page application using React 18, manage global state with Redux Toolkit, and handle client-side routing with React Router.

## Consequences
Delivers a responsive client experience and predictable state handling, but increases bundle complexity and requires careful performance tuning and SEO strategies for a SPA.