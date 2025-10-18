---
### ADR-006: Combine Material UI v5 and React-Bootstrap for UI components

Status: Inferred
Context: Dependencies include @mui/material, @mui/icons-material, @emotion/* (MUI v5 styling), and react-bootstrap/bootstrap. CSS files are co-located per component.
Decision: Use a blend of MUI components and React-Bootstrap for layout, styling, and widgets, supplemented by CSS files for custom styles.
Consequences:
- Positive: Rapid UI development leveraging familiar component libraries; access to a wide component set.
- Negative: Larger bundle size; potential design inconsistency and style conflicts; two styling systems to manage (Emotion/MUI and Bootstrap CSS); theming cohesion is harder.