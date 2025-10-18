# ADR-004: Selection of .NET for Serverless Function Implementation

**Date**: 2025-10-09
**Status**: Proposed

## Context
A specific technology stack was required to implement the custom skill logic within the Azure Function. The choice of language and runtime impacts developer productivity, performance, and ecosystem compatibility.

## Decision
The custom skill was implemented using .NET and C#. This aligns the custom component's technology with the broader Microsoft Azure platform on which the solution is built.

## Consequences
Using .NET provides excellent performance and first-class tooling support within the Azure ecosystem (e.g., Visual Studio integration, robust SDKs). This choice streamlines development for teams already skilled in the Microsoft stack. However, it may pose a barrier to entry for developers unfamiliar with .NET, even though Azure Functions support other languages.