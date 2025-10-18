# ADR-002: Selection of Node.js and TypeScript for the Backend

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project required a modern, popular, and accessible backend technology stack familiar to a wide range of web developers. As the codebase grew, a need for improved code quality, maintainability, and type safety became critical.

## Decision
The backend was built on Node.js using the Express.js framework. TypeScript was chosen over plain JavaScript to introduce static typing.

## Consequences
This decision leverages the vast NPM ecosystem and the flexibility of Express.js. TypeScript significantly enhances code quality, reduces runtime errors, and improves the developer experience through better tooling and code completion. The downside is a minor increase in build complexity due to the TypeScript compilation step.