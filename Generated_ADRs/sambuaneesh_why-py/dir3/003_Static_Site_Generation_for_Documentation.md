# ADR-003: Static Site Generation for Documentation

**Date**: 2025-10-11
**Status**: Proposed

## Context
To support the esoteric language, a comprehensive and user-friendly documentation website was necessary. The site needed to be fast, easy to maintain, and capable of including interactive elements.

## Decision
The Astro static site generator was selected, using the Starlight theme specifically designed for documentation. This stack uses a component-based architecture (JSX) to build a static HTML/CSS/JS site.

## Consequences
This decision yields a highly performant, SEO-friendly website with a professional look-and-feel provided by Starlight. Using Astro allows for the seamless integration of interactive JavaScript components on an otherwise static site, providing the best of both worlds: speed and interactivity.