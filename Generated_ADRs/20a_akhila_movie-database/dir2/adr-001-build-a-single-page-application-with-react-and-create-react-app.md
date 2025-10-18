### ADR-001: Build a single-page application with React and Create React App

Status: Inferred
Context: The repository contains a standard Create React App (CRA) layout with react-scripts, public assets, and src components. package.json uses react-scripts for start/build/test and React 17 as the UI framework.
Decision: Use React 17 and Create React App to scaffold and build the SPA.
Consequences: 
- Positive: Fast bootstrap, zero-config build tooling, sensible defaults, easy local development and deployment.
- Negative: Limited control over webpack without ejecting; constraints on advanced build customization.