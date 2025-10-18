# ADR-008: Next.js App Router with feature-aligned React components

**Date**: 2025-10-14
**Status**: Proposed

## Context
Frontend uses the Next.js app directory and components that map directly to backend capabilities (VisualOverview, InfographicSlides, EngagingReels, Podcast).

## Decision
Adopt Next.js App Router and build feature-specific, composable components aligned to backend outputs.

## Consequences
Pros: good co-evolution between UI and backend features; better routing/data-fetch ergonomics. Cons: requires discipline around server/client component boundaries; potential SSR/CSR complexities.