---
### ADR-003: Use styled-components for styling with per-component style files

Status: Inferred
Context: styled-components is a dependency. Each visual component has a corresponding *.styles.js file (e.g., Header.styles.js, Grid.styles.js), and a GlobalStyle.js is present.
Decision: Use styled-components for CSS-in-JS, co-locating styles with components and defining a GlobalStyle for app-wide styles.
Consequences:
- Positive: Scoped styles, dynamic theming, improved maintainability through co-location; avoids global CSS conflicts.
- Negative: Runtime styling cost, potential SSR considerations (if added later), and lock-in to styled-components conventions.