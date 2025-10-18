---
### ADR-003: Adopt shadcn/ui, Radix UI primitives, and TailwindCSS for the design system

Status: Inferred
Context: The codebase includes shadcn-style component files under src/components/ui, Radix UI dependencies, Tailwind configuration, and postcss setup. The product aims for accessible, consistent, yet customizable UI.
Decision: Compose the UI with shadcn/ui patterns over Radix primitives and style with TailwindCSS.
Consequences:
- Positive: Accessible components, consistent design tokens, full control over styling, local components reduce runtime deps.
- Negative: More responsibility for design tokens and component maintenance; potential bundle size growth if many components are included.