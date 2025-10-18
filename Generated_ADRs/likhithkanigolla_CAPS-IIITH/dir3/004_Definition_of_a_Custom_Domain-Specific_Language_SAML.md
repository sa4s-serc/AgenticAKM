# ADR-004: Definition of a Custom Domain-Specific Language (SAML)

**Date**: 2025-10-09
**Status**: Proposed

## Context
To enable high-level system modeling, a formal language was required to define components, their ports, and their interconnections, independent of the final implementation technology. Standard modeling languages like UML or SysML may have been too broad or cumbersome for the project's specific domain.

## Decision
A custom System Architecture Modeling Language (SAML) was created, with its formal structure defined via a PlantUML metamodel. This DSL serves as the canonical, high-level input for both the LLM and traditional transformation pipelines.

## Consequences
This provides a modeling language that is precisely tailored to the project's needs, simplifying the modeling process for system designers. It also gives the team full control over the language's evolution. The drawback is the significant investment required to design, document, and build tooling (parsers, generators) for a proprietary language.