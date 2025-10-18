---
### ADR-006: Composable UI with shadcn/ui and Tailwind CSS

**Status:** Inferred
**Context:** To build a consistent and polished user interface rapidly, a strategy for UI components was needed. Options included building all components from scratch, using a pre-styled component library (like Material-UI), or using a more flexible, composable approach.
**Decision:** A composable UI strategy was adopted using `shadcn/ui`, which is built on top of Radix UI primitives and styled with Tailwind CSS. This is inferred from the combination of dependencies (`tailwindcss`, numerous `@radix-ui/*` packages, `clsx`) and the file structure (`src/components/ui/`), where individual, un-packaged component source files are present (e.g., `button.tsx`, `card.tsx`).
**Consequences:**
*   **Positive:** This approach provides maximum flexibility and ownership. Developers have direct access to the component code, allowing for easy customization. It avoids style conflicts common with traditional UI libraries. The use of Tailwind CSS enables rapid, utility-first styling. The components are accessible out-of-the-box thanks to Radix UI.
*   **Negative:** Unlike a traditional library, updating components is a manual process (e.g., re-running the `shadcn/ui` CLI) rather than a simple package version bump. The initial setup is more involved than just installing a single dependency.