---
### ADR-004: Combine UI libraries to accelerate delivery (NativeBase, React Native Paper, Expo Vector Icons, and MUI for web)

Status: Inferred
Context: The app depends on NativeBase, React Native Paper, @expo/vector-icons, and @mui/material. Delivering UI quickly across mobile and web may require leveraging ready-made components from multiple ecosystems.
Decision: Use multiple UI libraries to balance design needs across native and web targets.
Consequences:
- Positive: Faster UI development using prebuilt components; flexibility to pick best-of-breed controls for each platform.
- Negative: Risk of inconsistent design language/themes, increased bundle size, overlapping dependencies, and more complex theming.