# ADR-002: Component Styling with CSS-in-JS

**Date**: 2025-10-10
**Status**: Proposed

## Context
A scalable and maintainable styling solution was needed that aligned with the component-based architecture, preventing global CSS scope conflicts and allowing for dynamic styling based on component state or props.

## Decision
A CSS-in-JS approach was chosen, implementing the `styled-components` library. This allows styles to be written in JavaScript, co-located with their respective components, and scoped automatically.

## Consequences
This decision ensures complete style encapsulation, eliminating class name collisions and making components truly portable. It also provides a powerful way to create dynamic styles based on props. The downsides include a minor runtime performance overhead and a potential learning curve for developers accustomed to traditional CSS.