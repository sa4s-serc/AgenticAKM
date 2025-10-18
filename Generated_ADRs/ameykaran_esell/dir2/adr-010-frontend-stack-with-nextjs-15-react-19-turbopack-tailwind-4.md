---
### ADR-010: Frontend stack with Next.js 15, React 19, Turbopack, Tailwind 4

Status: Inferred
Context: package.json specifies next 15.5.4, react 19.1.0, tailwindcss ^4; scripts use --turbopack; components for chat, PDF, reels, slides exist.
Decision: Build the UI with Next.js App Router, React 19, Turbopack for dev/build speed, and Tailwind CSS v4 for styling.
Consequences:
- Positive: Modern SSR/SSG capabilities; fast iterative development; strong ecosystem.
- Negative: Cutting-edge versions may have breaking changes; Turbopack maturity considerations; Tailwind v4 migration nuances.